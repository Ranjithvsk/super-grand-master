with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# ============================================================
# CHANGE 1: Add PROFILE view CSS
# ============================================================
old_css = "#btn-out{padding:5px 10px;background:none;border:1px solid #3a3632;border-radius:3px;color:#999;font-size:12px;cursor:pointer;font-family:inherit} #btn-out:hover{background:#302e2b;color:#fff} </style>"
new_css = """#btn-out{padding:5px 10px;background:none;border:1px solid #3a3632;border-radius:3px;color:#999;font-size:12px;cursor:pointer;font-family:inherit} #btn-out:hover{background:#302e2b;color:#fff}
/* PROFILE VIEW */
.profile-page{max-width:480px;margin:0 auto;padding:30px 12px}
.profile-avatar{width:80px;height:80px;border-radius:50%;background:#629924;display:flex;align-items:center;justify-content:center;font-size:32px;font-weight:800;color:#fff;margin:0 auto 16px;overflow:hidden}
.profile-avatar img{width:100%;height:100%;object-fit:cover}
.profile-name{font-size:22px;font-weight:800;color:#fff;text-align:center;margin-bottom:4px}
.profile-email{font-size:13px;color:#666;text-align:center;margin-bottom:6px}
.profile-role{display:inline-block;padding:2px 10px;border-radius:10px;font-size:11px;font-weight:700;text-transform:uppercase;margin-bottom:24px}
.profile-role.admin{background:#629924;color:#fff}
.profile-role.user{background:#302e2b;color:#999}
.profile-section{text-align:center;margin-bottom:24px}
.profile-stats{display:grid;grid-template-columns:repeat(2,1fr);gap:10px;margin-bottom:24px}
.profile-stat{background:#262421;border-radius:6px;padding:18px;text-align:center}
.profile-stat .num{font-size:30px;font-weight:800;color:#629924}
.profile-stat .lbl{font-size:11px;color:#999;text-transform:uppercase;letter-spacing:.5px;margin-top:3px}
.profile-joined{font-size:12px;color:#555;text-align:center;margin-top:8px}
.profile-sync-note{font-size:12px;color:#629924;text-align:center;margin-bottom:16px}
</style>"""

if old_css in src:
    src = src.replace(old_css, new_css)
    print("CHANGE 1 done: Profile CSS added")
else:
    print("CHANGE 1 WARNING: CSS anchor not found")

# ============================================================
# CHANGE 2: Add PROFILE nav button and view HTML
# ============================================================
old_nav = '<a onclick="switchView(\'stats\')">STATS</a>'
new_nav = '<a onclick="switchView(\'stats\')">STATS</a>\n    <a onclick="switchView(\'profile\')">PROFILE</a>'

if old_nav in src:
    src = src.replace(old_nav, new_nav)
    print("CHANGE 2a done: Profile nav button added")
else:
    print("CHANGE 2a WARNING: nav anchor not found")

old_stats_view = '<!-- STATS VIEW -->'
new_profile_view = """<!-- PROFILE VIEW -->
<div class="profile-page hidden" id="v-profile">
  <div class="profile-section">
    <div class="profile-avatar" id="pav"><span id="pini">?</span></div>
    <div class="profile-name" id="pname">—</div>
    <div class="profile-email" id="pemail">—</div>
    <span class="profile-role" id="prole">user</span>
  </div>
  <div class="profile-stats">
    <div class="profile-stat"><div class="num" id="ppS">0</div><div class="lbl">Puzzles Solved</div></div>
    <div class="profile-stat"><div class="num" id="ppA">0%</div><div class="lbl">Accuracy</div></div>
    <div class="profile-stat"><div class="num" id="ppK">0</div><div class="lbl">Best Streak</div></div>
    <div class="profile-stat"><div class="num" id="ppG">0</div><div class="lbl">Games Played</div></div>
  </div>
  <div class="profile-sync-note" id="psync">Stats synced to cloud ☁</div>
  <div class="profile-joined" id="pjoined"></div>
</div>

<!-- STATS VIEW -->"""

if '<!-- STATS VIEW -->' in src:
    src = src.replace('<!-- STATS VIEW -->', new_profile_view)
    print("CHANGE 2b done: Profile view HTML added")
else:
    print("CHANGE 2b WARNING: stats view anchor not found")

# ============================================================
# CHANGE 3: Update switchView() to handle profile + load DB stats
# ============================================================
old_switch = """function switchView(v){
  view=v;
  document.querySelectorAll('.site-buttons a').forEach(a=>{a.classList.toggle('active',a.textContent.toLowerCase()===v)});
  document.getElementById('v-puzzles').classList.toggle('hidden',v!=='puzzles');
  document.getElementById('v-play').classList.toggle('hidden',v!=='play');
  document.getElementById('v-stats').classList.toggle('hidden',v!=='stats');
  if(v==='stats')updStats();
}"""

new_switch = """function switchView(v){
  view=v;
  document.querySelectorAll('.site-buttons a').forEach(a=>{a.classList.toggle('active',a.textContent.toLowerCase()===v)});
  document.getElementById('v-puzzles').classList.toggle('hidden',v!=='puzzles');
  document.getElementById('v-play').classList.toggle('hidden',v!=='play');
  document.getElementById('v-stats').classList.toggle('hidden',v!=='stats');
  document.getElementById('v-profile').classList.toggle('hidden',v!=='profile');
  if(v==='stats')updStats();
  if(v==='profile')updProfile();
}"""

if old_switch in src:
    src = src.replace(old_switch, new_switch)
    print("CHANGE 3 done: switchView updated for profile")
else:
    print("CHANGE 3 WARNING: switchView anchor not found")

# ============================================================
# CHANGE 4: Replace saveSt() with version that also syncs to Firebase
# ============================================================
old_saveSt = "function saveSt(){localStorage.setItem('sgm3',JSON.stringify(st))}"
new_saveSt = """function saveSt(){
  localStorage.setItem('sgm3',JSON.stringify(st));
  // Sync to Firebase if logged in
  try{
    const u=firebase.auth().currentUser;
    if(u) firebase.database().ref('users/'+u.uid+'/stats').set({s:st.s,a:st.a,k:st.k,g:st.g,w:st.w,updated:new Date().toISOString()});
  }catch(e){}
}
function updProfile(){
  const u=firebase.auth().currentUser;
  if(!u)return;
  const isAdmin=['ranjith.vsk@gmail.com'].includes(u.email);
  document.getElementById('pname').textContent=u.displayName||u.email.split('@')[0];
  document.getElementById('pemail').textContent=u.email;
  document.getElementById('pini').textContent=(u.displayName||u.email)[0].toUpperCase();
  const roleEl=document.getElementById('prole');
  roleEl.textContent=isAdmin?'Admin':'User';
  roleEl.className='profile-role '+(isAdmin?'admin':'user');
  if(u.photoURL){document.getElementById('pav').innerHTML='<img src="'+u.photoURL+'" alt="avatar"/>';}
  // Load stats from Firebase
  firebase.database().ref('users/'+u.uid+'/stats').once('value').then(snap=>{
    const d=snap.val();
    if(d){
      // Merge Firebase stats with local (take max of each)
      st.s=Math.max(st.s,d.s||0);st.a=Math.max(st.a,d.a||0);
      st.k=Math.max(st.k,d.k||0);st.g=Math.max(st.g,d.g||0);
      localStorage.setItem('sgm3',JSON.stringify(st));
    }
    const acc=st.a>0?Math.round(st.s/st.a*100):0;
    document.getElementById('ppS').textContent=st.s;
    document.getElementById('ppA').textContent=acc+'%';
    document.getElementById('ppK').textContent=st.k;
    document.getElementById('ppG').textContent=st.g;
    document.getElementById('psync').textContent='Stats synced to cloud \u2601';
  }).catch(()=>{
    const acc=st.a>0?Math.round(st.s/st.a*100):0;
    document.getElementById('ppS').textContent=st.s;
    document.getElementById('ppA').textContent=acc+'%';
    document.getElementById('ppK').textContent=st.k;
    document.getElementById('ppG').textContent=st.g;
    document.getElementById('psync').textContent='Showing local stats';
  });
  // Load join date
  firebase.database().ref('users/'+u.uid+'/lastLogin').once('value').then(snap=>{
    const d=snap.val();
    if(d) document.getElementById('pjoined').textContent='Last login: '+new Date(d).toLocaleDateString();
  });
}"""

if old_saveSt in src:
    src = src.replace(old_saveSt, new_saveSt)
    print("CHANGE 4 done: saveSt() now syncs to Firebase + updProfile() added")
else:
    print("CHANGE 4 WARNING: saveSt anchor not found")

# ============================================================
# CHANGE 5: Load stats FROM Firebase on login (onAuthStateChanged)
# ============================================================
old_db_update = """      db.ref('users/'+user.uid).update({
        email:user.email,
        name:user.displayName||user.email.split('@')[0],
        role:isAdmin?'admin':'user',
        lastLogin:new Date().toISOString()
      });"""

new_db_update = """      db.ref('users/'+user.uid).update({
        email:user.email,
        name:user.displayName||user.email.split('@')[0],
        role:isAdmin?'admin':'user',
        lastLogin:new Date().toISOString()
      });
      // Load stats from Firebase and merge with local
      db.ref('users/'+user.uid+'/stats').once('value').then(snap=>{
        const d=snap.val();
        if(d){
          st.s=Math.max(st.s,d.s||0);st.a=Math.max(st.a,d.a||0);
          st.k=Math.max(st.k,d.k||0);st.g=Math.max(st.g,d.g||0);
          localStorage.setItem('sgm3',JSON.stringify(st));
        }
      });"""

if old_db_update in src:
    src = src.replace(old_db_update, new_db_update)
    print("CHANGE 5 done: Stats loaded from Firebase on login")
else:
    print("CHANGE 5 WARNING: db.ref anchor not found")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("\nAll done! Run: git add . && git commit -m 'Add profile page + Firebase stats sync' && git push origin HEAD:main")
