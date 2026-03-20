<template>
  <div class="auth">
    <!-- 装饰元素 -->
    <div class="decoration">🌾</div>
    <div class="decoration">🥕</div>
    <div class="decoration">🍅</div>
    
    <header>
      <div class="logo">
        <div class="logo-icon">🏡</div>
        <div>
          <h1>星露谷邻里互助</h1>
          <p class="subtitle">Stardew Valley Neighborhood Aid</p>
        </div>
      </div>
    </header>
    
    <nav>
      <div class="nav-container">
        <router-link to="/" class="nav-item">
          <span>🏠</span> 首页
        </router-link>
        <a href="#" class="nav-item">
          <span>📋</span> 互助任务
        </a>
        <a href="#" class="nav-item">
          <span>👥</span> 邻里成员
        </a>
        <a href="#" class="nav-item">
          <span>📅</span> 活动日历
        </a>
        <a href="#" class="nav-item">
          <span>💬</span> 社区论坛
        </a>
        <router-link to="/auth" class="nav-item">
          <span>⚙️</span> 登录/注册
        </router-link>
      </div>
    </nav>
    
    <main>
      <section class="auth-section">
        <div class="auth-card">
          <div class="auth-header">
            <h2>{{ isLogin ? '登录' : '注册' }}</h2>
            <p class="auth-subtitle">{{ isLogin ? '欢迎回来，星露谷居民！' : '加入我们的社区，开始互助之旅！' }}</p>
          </div>
          
          <div class="auth-tabs">
            <button class="tab-button" :class="{ active: isLogin }" @click="isLogin = true">
              登录
            </button>
            <button class="tab-button" :class="{ active: !isLogin }" @click="isLogin = false">
              注册
            </button>
          </div>
          
          <form class="auth-form" @submit.prevent="handleSubmit">
            <div class="form-group" v-if="!isLogin">
              <label>用户名</label>
              <input type="text" v-model="form.username" required />
            </div>
            
            <div class="form-group">
              <label>邮箱</label>
              <input type="email" v-model="form.email" required />
            </div>
            
            <div class="form-group">
              <label>密码</label>
              <input type="password" v-model="form.password" required />
            </div>
            
            <div class="form-group" v-if="!isLogin">
              <label>确认密码</label>
              <input type="password" v-model="form.confirmPassword" required />
            </div>
            
            <button type="submit" class="submit-button">
              {{ isLogin ? '登录' : '注册' }}
            </button>
          </form>
        </div>
      </section>
    </main>
    
    <footer>
      <p>© 2024 星露谷邻里互助 · 让我们的社区更加温暖</p>
      <p style="margin-top: 10px; font-size: 14px; opacity: 0.8;">
        Inspired by Stardew Valley · Made with ❤️ for our community
      </p>
    </footer>
    
    <!-- 提示框 -->
    <div v-if="showToast" class="toast" @click="closeToast">
      {{ toastMessage }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'Auth',
  data() {
    return {
      isLogin: true,
      form: {
        username: '',
        email: '',
        password: '',
        confirmPassword: ''
      },
      showToast: false,
      toastMessage: ''
    }
  },
  methods: {
    handleSubmit() {
      if (!this.isLogin && this.form.password !== this.form.confirmPassword) {
        this.showToastMessage('两次输入的密码不一致！');
        return;
      }
      
      // 模拟登录/注册成功
      if (this.isLogin) {
        // 登录成功
        localStorage.setItem('access_token', 'mock_token');
        this.$router.push('/profile');
      } else {
        // 注册成功
        this.showToastMessage('注册成功！请登录');
        this.isLogin = true;
      }
    },
    showToastMessage(message) {
      this.toastMessage = message;
      this.showToast = true;
      setTimeout(() => {
        this.showToast = false;
      }, 3000);
    },
    closeToast() {
      this.showToast = false;
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Microsoft YaHei', sans-serif;
  background: linear-gradient(to bottom, #87CEEB 0%, #98D98E 50%, #8B7355 100%);
  min-height: 100vh;
  position: relative;
  overflow-x: hidden;
}

/* 头部 */
header {
  background: rgba(255, 255, 255, 0.95);
  padding: 20px;
  text-align: center;
  position: relative;
  z-index: 100;
}

.logo {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 15px;
  margin-bottom: 10px;
}

.logo-icon {
  width: 60px;
  height: 60px;
  background: #8B4513;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 30px;
  border: 3px solid #654321;
}

h1 {
  font-family: 'Press Start 2P', cursive;
  font-size: 24px;
  color: #2d5016;
  text-shadow: 2px 2px 0 #fff;
}

.subtitle {
  color: #5a7c47;
  font-size: 16px;
  margin-top: 5px;
}

/* 导航栏 */
nav {
  background: rgba(45, 80, 22, 0.9);
  padding: 15px;
  position: sticky;
  top: 0;
  z-index: 99;
  box-shadow: 0 2px 10px rgba(0,0,0,0.2);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  gap: 30px;
  flex-wrap: wrap;
}

.nav-item {
  color: #fff;
  text-decoration: none;
  padding: 8px 20px;
  border: 2px solid #fff;
  border-radius: 20px;
  transition: all 0.3s;
  font-weight: bold;
  display: flex;
  align-items: center;
  gap: 8px;
}

.nav-item:hover {
  background: #fff;
  color: #2d5016;
  transform: translateY(-2px);
}

/* 主要内容区 */
main {
  max-width: 1200px;
  margin: 30px auto;
  padding: 0 20px;
}

/* 认证区域 */
.auth-section {
  display: flex;
  justify-content: center;
  margin-bottom: 40px;
}

.auth-card {
  background: rgba(255, 255, 255, 0.95);
  border-radius: 15px;
  padding: 30px;
  width: 100%;
  max-width: 500px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.1);
}

.auth-header {
  text-align: center;
  margin-bottom: 30px;
}

.auth-header h2 {
  color: #2d5016;
  font-size: 24px;
  margin-bottom: 10px;
}

.auth-subtitle {
  color: #5a7c47;
  font-size: 16px;
}

/* 标签页 */
.auth-tabs {
  display: flex;
  gap: 10px;
  margin-bottom: 30px;
  border-bottom: 2px solid #8B4513;
  padding-bottom: 10px;
}

.tab-button {
  flex: 1;
  padding: 12px;
  border: none;
  background: transparent;
  color: #5a7c47;
  font-weight: bold;
  cursor: pointer;
  transition: all 0.3s;
  border-radius: 5px;
}

.tab-button:hover {
  background: #f9f5eb;
}

.tab-button.active {
  background: #8B4513;
  color: #fff;
}

/* 表单 */
.auth-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 5px;
}

.form-group label {
  color: #2d5016;
  font-weight: bold;
  font-size: 14px;
}

.form-group input {
  padding: 12px;
  border: 2px solid #8B4513;
  border-radius: 5px;
  font-size: 16px;
}

.submit-button {
  padding: 14px;
  background: #8B4513;
  color: #fff;
  border: none;
  border-radius: 5px;
  font-weight: bold;
  font-size: 16px;
  cursor: pointer;
  transition: all 0.3s;
  margin-top: 10px;
}

.submit-button:hover {
  background: #654321;
  transform: translateY(-2px);
}

/* 页脚 */
footer {
  background: rgba(45, 80, 22, 0.9);
  color: #fff;
  text-align: center;
  padding: 30px;
  margin-top: 50px;
}

/* 装饰元素 */
.decoration {
  position: fixed;
  font-size: 30px;
  animation: float 6s ease-in-out infinite;
  z-index: 1;
  opacity: 0.3;
}

.decoration:nth-child(1) {
  top: 20%;
  left: 5%;
  animation-delay: 0s;
}

.decoration:nth-child(2) {
  top: 60%;
  right: 5%;
  animation-delay: 2s;
}

.decoration:nth-child(3) {
  bottom: 20%;
  left: 10%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-20px);
  }
}

/* 提示框 */
.toast {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: rgba(45, 80, 22, 0.95);
  color: white;
  padding: 20px 30px;
  border-radius: 10px;
  box-shadow: 0 5px 20px rgba(0,0,0,0.3);
  z-index: 1000;
  max-width: 400px;
  text-align: center;
  animation: fadeIn 0.3s ease-out;
  cursor: pointer;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translate(-50%, -50%) translateY(20px);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%) translateY(0);
  }
}

/* 响应式设计 */
@media (max-width: 768px) {
  .auth-card {
    padding: 20px;
  }
  
  .auth-header h2 {
    font-size: 20px;
  }
  
  .form-group input {
    padding: 10px;
  }
  
  .submit-button {
    padding: 12px;
  }
}
</style>