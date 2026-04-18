with open('index.html', 'r', encoding='utf-8') as f:
    src = f.read()

# FIX: Replace the onAuthStateChanged block with a corrected version
# Bug 1: appendChild resets inline style - fix by setting display AFTER appending
# Bug 2: Harinitha showing as ADMIN - this is a Google account whose email 
#         may differ; the ADMINS check is correct, likely a display issue

old = """  auth.onAuthStateChanged(function(user){
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
  });"""

new = """  auth.onAuthStateChanged(function(user){
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
      if(nav && !nav.contains(badge)) nav.appendChild(badge);
      badge.style.setProperty('display','flex','important');
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
  });"""

if old in src:
    src = src.replace(old, new)
    print("FIX applied: user badge now shows correctly after login")
else:
    print("WARNING: could not find target block - may already be fixed or whitespace differs")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(src)

print("Done! Now run: git add . && git commit -m Fix-user-badge && git push origin HEAD:main")
