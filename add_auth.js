const fs = require('fs');

const filePath = 'G:\\My Drive\\Super Grand Master\\index.html';
let html = fs.readFileSync(filePath, 'utf8');

// 1. Add Firebase Auth SDK after existing scripts in <head>
const firebaseSDK = `
  <!-- Firebase Auth SDK -->
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-app-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-auth-compat.js"></script>
  <script src="https://www.gstatic.com/firebasejs/10.8.0/firebase-database-compat.js"></script>
`;

html = html.replace('</head>', firebaseSDK + '</head>');

// 2. Add auth CSS before </style>
const authCSS = `
/* ===== AUTH OVERLAY ===== */
#auth-overlay {
  position: fixed; inset: 0; background: #161512;
  z-index: 9999; display: flex; align-items: center;
  justify-content: center; flex-direction: column;
}
#auth-box {
  background: #262421; border-radius: 8px;
  padding: 40px 36px; width: 100%; max-width: 360px;
  box-shadow: 0 8px 32px rgba(0,0,0,0.5);
  text-align: center;
}
#auth-box .logo { font-size: 32px; margin-bottom: 6px; }
#auth-box h2 { color: #fff; font-size: 22px; margin-bottom: 4px; }
#auth-box p { color: #777; font-size: 13px; margin-bottom: 28px; }
#auth-box input {
  width: 100%; padding: 11px 14px; margin-bottom: 12px;
  background: #302e2b; border: 1px solid #3a3632;
  border-radius: 4px; color: #fff; font-size: 15px;
  font-family: 'Noto Sans', sans-serif; outline: none;
  transition: border-color .2s;
}
#auth-box input:focus { border-color: #3692e7; }
#auth-box .btn-signin {
  width: 100%; padding: 12px; background: #629924;
  color: #fff; border: none; border-radius: 4px;
  font-size: 15px; font-weight: 700; cursor: pointer;
  font-family: 'Noto Sans', sans-serif; margin-bottom: 14px;
  transition: background .2s;
}
#auth-box .btn-signin:hover { background: #72b328; }
#auth-box .btn-google {
  width: 100%; padding: 11px; background: #fff;
  color: #333; border: none; border-radius: 4px;
  font-size: 14px; font-weight: 600; cursor: pointer;
  font-family: 'Noto Sans', sans-serif; display: flex;
  align-items: center; justify-content: center; gap: 10px;
  transition: background .2s;
}
#auth-box .btn-google:hover { background: #f0f0f0; }
#auth-box .divider {
  display: flex; align-items: center; gap: 10px;
  margin: 14px 0; color: #555; font-size: 12px;
}
#auth-box .divider::before,
#auth-box .divider::after {
  content: ''; flex: 1; height: 1px; background: #3a3632;
}
#auth-box .err { color: #e74c3c; font-size: 13px; margin-bottom: 10px; min-height: 18px; }
#auth-box .toggle { color: #3692e7; font-size: 13px; cursor: pointer; margin-top: 14px; }
#auth-box .toggle:hover { text-decoration: underline; }

/* User badge in nav */
#user-badge {
  display: none; align-items: center; gap: 8px;
  margin-left: auto; color: #bababa; font-size: 13px;
}
#user-badge .avatar {
  width: 28px; height: 28px; border-radius: 50%;
  background: #629924; display: flex; align-items: center;
  justify-content: center; font-weight: 700; font-size: 13px;
  color: #fff; overflow: hidden;
}
#user-badge .avatar img { width: 100%; height: 100%; object-fit: cover; }
#user-badge .uname { color: #ddd; font-weight: 600; }
#user-badge .admin-badge {
  background: #629924; color: #fff; font-size: 10px;
  font-weight: 700; padding: 2px 6px; border-radius: 10px;
  text-transform: uppercase; letter-spacing: .5px;
}
#btn-signout {
  padding: 5px 10px; background: none; border: 1px solid #3a3632;
  border-radius: 3px; color: #999; font-size: 12px;
  cursor: pointer; font-family: 'Noto Sans', sans-serif;
}
#btn-signout:hover { background: #302e2b; color: #fff; }
`;

html = html.replace('</style>', authCSS + '\n</style>');

// 3. Add auth HTML overlay before </body>
const authHTML = `
<!-- ===== AUTH OVERLAY ===== -->
<div id="auth-overlay">
  <div id="auth-box">
    <div class="logo">♞</div>
    <h2>Super Grand Master</h2>
    <p>Sign in to track your progress</p>
    <div class="err" id="auth-err"></div>
    <input type="email" id="auth-email" placeholder="Email address" autocomplete="email"/>
    <input type="password" id="auth-pw" placeholder="Password" autocomplete="current-password"/>
    <button class="btn-signin" id="btn-email-signin">Sign In</button>
    <div class="divider">or</div>
    <button class="btn-google" id="btn-google-signin">
      <svg width="18" height="18" viewBox="0 0 48 48"><path fill="#EA4335" d="M24 9.5c3.54 0 6.71 1.22 9.21 3.6l6.85-6.85C35.9 2.38 30.47 0 24 0 14.62 0 6.51 5.38 2.56 13.22l7.98 6.19C12.43 13.72 17.74 9.5 24 9.5z"/><path fill="#4285F4" d="M46.98 24.55c0-1.57-.15-3.09-.38-4.55H24v9.02h12.94c-.58 2.96-2.26 5.48-4.78 7.18l7.73 6c4.51-4.18 7.09-10.36 7.09-17.65z"/><path fill="#FBBC05" d="M10.53 28.59c-.48-1.45-.76-2.99-.76-4.59s.27-3.14.76-4.59l-7.98-6.19C.92 16.46 0 20.12 0 24c0 3.88.92 7.54 2.56 10.78l7.97-6.19z"/><path fill="#34A853" d="M24 48c6.48 0 11.93-2.13 15.89-5.81l-7.73-6c-2.15 1.45-4.92 2.3-8.16 2.3-6.26 0-11.57-4.22-13.47-9.91l-7.98 6.19C6.51 42.62 14.62 48 24 48z"/></svg>
      Continue with Google
    </button>
    <div class="toggle" id="auth-toggle">Don't have an account? Sign up</div>
  </div>
</div>

<!-- User badge (shown in nav after login) -->
<div id="user-badge">
  <div class="avatar" id="user-avatar"><span id="user-initial">U</span></div>
  <span class="uname" id="user-name"></span>
  <span class="admin-badge" id="admin-badge" style="display:none">Admin</span>
  <button id="btn-signout">Sign out</button>
</div>
`;

html = html.replace('</body>', authHTML + '\n</body>');

// 4. Add auth JS before </body>
const authJS = `
<script>
// ===== FIREBASE AUTH =====
const FIREBASE_CONFIG = {
  apiKey: "AIzaSyCA8oHffDPJP3fXGbQ5zJupPVJ0KsV7dhU",
  authDomain: "super-grand-master.firebaseapp.com",
  projectId: "super-grand-master",
  storageBucket: "super-grand-master.firebasestorage.app",
  messagingSenderId: "663805467661",
  appId: "1:663805467661:web:5d6e6584d3142b749d4944",
  databaseURL: "https://super-grand-master-default-rtdb.asia-southeast1.firebasedatabase.app"
};

// Only init if not already initialized
if (!firebase.apps.length) firebase.initializeApp(FIREBASE_CONFIG);
const auth = firebase.auth();
const db = firebase.database();

// Admin emails
const ADMINS = ['ranjith.vsk@gmail.com'];

let isSignUp = false;

// Toggle sign in / sign up
document.getElementById('auth-toggle').onclick = () => {
  isSignUp = !isSignUp;
  document.getElementById('btn-email-signin').textContent = isSignUp ? 'Create Account' : 'Sign In';
  document.getElementById('auth-toggle').textContent = isSignUp
    ? 'Already have an account? Sign in'
    : "Don't have an account? Sign up";
  document.getElementById('auth-err').textContent = '';
};

// Email sign in / sign up
document.getElementById('btn-email-signin').onclick = async () => {
  const email = document.getElementById('auth-email').value.trim();
  const pw = document.getElementById('auth-pw').value;
  const errEl = document.getElementById('auth-err');
  errEl.textContent = '';
  if (!email || !pw) { errEl.textContent = 'Please enter email and password.'; return; }
  try {
    if (isSignUp) {
      await auth.createUserWithEmailAndPassword(email, pw);
    } else {
      await auth.signInWithEmailAndPassword(email, pw);
    }
  } catch(e) {
    errEl.textContent = e.message.replace('Firebase: ', '').replace(/ \\(auth\\/.*\\)/, '');
  }
};

// Google sign in
document.getElementById('btn-google-signin').onclick = async () => {
  const provider = new firebase.auth.GoogleAuthProvider();
  try {
    await auth.signInWithPopup(provider);
  } catch(e) {
    document.getElementById('auth-err').textContent = e.message;
  }
};

// Sign out
document.getElementById('btn-signout').onclick = () => auth.signOut();

// Enter key on password
document.getElementById('auth-pw').addEventListener('keydown', e => {
  if (e.key === 'Enter') document.getElementById('btn-email-signin').click();
});

// Auth state listener
auth.onAuthStateChanged(user => {
  const overlay = document.getElementById('auth-overlay');
  const badge = document.getElementById('user-badge');
  const navButtons = document.querySelector('#top .site-buttons');

  if (user) {
    // Hide overlay, show app
    overlay.style.display = 'none';

    // Update user badge
    const isAdmin = ADMINS.includes(user.email);
    document.getElementById('user-name').textContent = user.displayName || user.email.split('@')[0];
    document.getElementById('user-initial').textContent = (user.displayName || user.email)[0].toUpperCase();
    document.getElementById('admin-badge').style.display = isAdmin ? 'inline-flex' : 'none';

    // Show photo if available
    if (user.photoURL) {
      document.getElementById('user-avatar').innerHTML = '<img src="' + user.photoURL + '" alt="avatar"/>';
    }

    // Move badge into nav
    badge.style.display = 'flex';
    navButtons.appendChild(badge);

    // Save user to DB
    const userRef = db.ref('users/' + user.uid);
    userRef.update({
      email: user.email,
      name: user.displayName || user.email.split('@')[0],
      role: isAdmin ? 'admin' : 'user',
      lastLogin: new Date().toISOString()
    });

    console.log('Signed in:', user.email, isAdmin ? '(ADMIN)' : '(user)');
  } else {
    // Show overlay
    overlay.style.display = 'flex';
    badge.style.display = 'none';
  }
});
</script>
`;

html = html.replace('</body>', authJS + '\n</body>');

fs.writeFileSync(filePath, html, 'utf8');
console.log('✅ Firebase Auth added to index.html!');
console.log('');
console.log('Next steps:');
console.log('1. Enable Email/Password and Google auth in Firebase Console');
console.log('2. git add . && git commit -m "Add Firebase Auth" && git push origin HEAD:main');
