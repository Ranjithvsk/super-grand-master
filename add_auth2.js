const fs = require('fs');
let h = fs.readFileSync('index.html', 'utf8');

// AUTH CSS
const css = `
#auth-overlay{position:fixed;inset:0;background:#161512;z-index:9999;display:flex;align-items:center;justify-content:center}
#auth-box{background:#262421;border-radius:8px;padding:40px 36px;width:100%;max-width:360px;text-align:center;box-shadow:0 8px 32px rgba(0,0,0,.5)}
#auth-box .logo{font-size:40px;margin-bottom:8px}
#auth-box h2{color:#fff;font-size:22px;margin-bottom:4px;font-weight:800}
#auth-box .sub{color:#666;font-size:13px;margin-bottom:24px}
#auth-box input{width:100%;padding:11px 14px;margin-bottom:10px;background:#302e2b;border:1px solid #3a3632;border-radius:4px;color:#fff;font-size:15px;font-family:inherit;outline:none;box-sizing:border-box}
#auth-box input:focus{border-color:#3692e7}
#auth-box .btn-email{width:100%;padding:12px;background:#629924;color:#fff;border:none;border-radius:4px;font-size:15px;font-weight:700;cursor:pointer;font-family:inherit;margin-bottom:12px}
#auth-box .btn-email:hover{background:#72b328}
#auth-box .btn-google{width:100%;padding:11px;background:#fff;color:#333;border:none;border-radius:4px;font-size:14px;font-weight:600;cursor:pointer;font-family:inherit;display:flex;align-items:center;justify-content:center;gap:10px;box-sizing:border-box}
#auth-box .btn-google:hover{background:#f0f0f0}
#auth-box .divider{display:flex;align-items:center;gap:10px;margin:12px 0;color:#555;font-size:12px}
#auth-box .divider::before,#auth-box .divider::after{content:'';flex:1;height:1px;background:#3a3632}
#auth-box .err{color:#e74c3c;font-size:13px;margin-bottom:8px;min-height:18px}
#auth-box .toggle{color:#3692e7;font-size:13px;cursor:pointer;margin-top:12px;display:inline-block}
#auth-box .toggle:hover{text-decoration:underline}
#user-badge{display:none;align-items:center;gap:8px;margin-left:auto}
#user-badge .av{width:28px;height:28px;border-radius:50%;background:#629924;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:13px;color:#fff;overflow:hidden;flex-shrink:0}
#user-badge .av img{width:100%;height:100%;object-fit:cover}
#user-badge .uname{color:#ddd;font-size:13px;font-weight:600}
#user-badge .abadge{background:#629924;color:#fff;font-size:10px;font-weight:700;padding:2px 6px;border-radius:10px;text-transform:uppercase}
#btn-out{padding:5px 10px;background:none;border:1px solid #3a3632;border-radius:3px;color:#999;font-size:12px;cursor:pointer;font-family:inherit}
#btn-out:hover{background:#302e2b;color:#fff}
`;

// AUTH HTML
const html_auth = `
<div id="auth-overlay">
  <div id="auth-box">
    <div class="logo">♞</div>
    <h2>Super Grand Master</h2>
    <p class="sub">Sign in to track your progress</p>
    <div class="err" id="aerr"></div>
    <input type="email" id="aem" placeholder="Email address" autocomplete="email"/>
    <input type="password" id="apw" placeholder="Password" autocomplete="current-password"/>
    <button class="btn-email" id="abtn">Sign In</button>
    <div class="divider">or</div>
    <button class="btn-google" id="agoog">
      <svg width="18" height="18" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
      Continue with Google
    </button>
    <span class="toggle" id="atog">Don't have an account? Sign up</span>
  </div>
</div>
<div id="user-badge">
  <div class="av" id="uav"><span id="uini">U</span></div>
  <span class="uname" id="uname"></span>
  <span class="abadge" id="abadge" style="display:none">Admin</span>
  <button id="btn-out">Sign out</button>
</div>
`;

// AUTH JS
const js_auth = `
<script>
(function(){
  const ADMINS=['ranjith.vsk@gmail.com'];
  const auth=firebase.auth();
  const db=firebase.database();
  let isUp=false;

  document.getElementById('atog').onclick=function(){
    isUp=!isUp;
    document.getElementById('abtn').textContent=isUp?'Create Account':'Sign In';
    document.getElementById('atog').textContent=isUp?'Already have an account? Sign in':"Don't have an account? Sign up";
    document.getElementById('aerr').textContent='';
  };

  document.getElementById('abtn').onclick=async function(){
    const em=document.getElementById('aem').value.trim();
    const pw=document.getElementById('apw').value;
    const err=document.getElementById('aerr');
    err.textContent='';
    if(!em||!pw){err.textContent='Please enter email and password.';return;}
    try{
      if(isUp) await auth.createUserWithEmailAndPassword(em,pw);
      else await auth.signInWithEmailAndPassword(em,pw);
    }catch(e){err.textContent=e.message.replace('Firebase: ','').replace(/ \\(auth\\/[^)]+\\)/,'');}
  };

  document.getElementById('agoog').onclick=async function(){
    try{await auth.signInWithPopup(new firebase.auth.GoogleAuthProvider());}
    catch(e){document.getElementById('aerr').textContent=e.message;}
  };

  document.getElementById('btn-out').onclick=function(){auth.signOut();};

  document.getElementById('apw').addEventListener('keydown',function(e){
    if(e.key==='Enter') document.getElementById('abtn').click();
  });

  auth.onAuthStateChanged(function(user){
    const ov=document.getElementById('auth-overlay');
    const badge=document.getElementById('user-badge');
    const nav=document.querySelector('#top .site-buttons');
    if(user){
      ov.style.display='none';
      const isAdmin=ADMINS.includes(user.email);
      document.getElementById('uname').textContent=user.displayName||user.email.split('@')[0];
      document.getElementById('uini').textContent=(user.displayName||user.email)[0].toUpperCase();
      document.getElementById('abadge').style.display=isAdmin?'inline-flex':'none';
      if(user.photoURL) document.getElementById('uav').innerHTML='<img src="'+user.photoURL+'" alt="avatar"/>';
      badge.style.display='flex';
      if(nav && !nav.contains(badge)) nav.appendChild(badge);
      db.ref('users/'+user.uid).update({
        email:user.email,
        name:user.displayName||user.email.split('@')[0],
        role:isAdmin?'admin':'user',
        lastLogin:new Date().toISOString()
      });
    } else {
      ov.style.display='flex';
      badge.style.display='none';
    }
  });
})();
</script>
`;

// Inject CSS
h = h.replace('</style>', css + '\n</style>');

// Inject HTML before </body>
h = h.replace('</body>', html_auth + '\n</body>');

// Inject JS before </body>
h = h.replace('</body>', js_auth + '\n</body>');

fs.writeFileSync('index.html', h);
const h2 = fs.readFileSync('index.html', 'utf8');
console.log('auth-overlay added:', h2.includes('auth-overlay'));
console.log('auth JS added:', h2.includes('auth.signInWithEmailAndPassword'));
console.log('length:', h2.length);
console.log('✅ Done! Now run: git add . && git commit -m "Add Firebase Auth UI" && git push origin HEAD:main');
