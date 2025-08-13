import { createI18n } from 'vue-i18n'

const messages = {
  zh: {
    home: {
      title: '欢迎来到 ANiTalk',
      desc: '一个全新的虚拟角色交流平台，让您与AI角色进行自然、有趣的对话 ✨',
      start: '网页端体验',
      more: '了解更多'
    },
    navbar: {
      home: '首页',
      download: '下载',
      login: '登录',
      register: '注册',
      userCenter: '用户中心',
      logout: '退出登录'
    },
    download: {
      title: '下载 ANiTalk',
      desc: '选择您喜欢的平台，开始与虚拟角色进行有趣的对话吧！ 🎉',
      pc: 'PC 客户端',
      android: '安卓 APP',
      pcDesc: '适用于 Windows 和 macOS 系统\n功能完整，体验最佳',
      androidDesc: '适用于 Android 设备\n随时随地，畅聊无阻',
      hd: '高清画质',
      plugin: '桌面插件',
      storage: '本地存储',
      fast: '轻量快速',
      widget: '桌面小组件',
      cloud: '云端同步',
      downloadPC: '下载 PC 版本 📥',
      downloadAndroid: '下载安卓版本 📥',
      sysreq: '系统要求',
      pcReq: 'PC 客户端',
      androidReq: '安卓 APP',
      win: 'Windows 10 或更高版本',
      mac: 'macOS 10.14 或更高版本',
      ram4: '4GB RAM 或更多',
      disk2: '2GB 可用存储空间',
      andver: 'Android 8.0 或更高版本',
      ram2: '2GB RAM 或更多',
      disk500: '500MB 可用存储空间',
      net: '网络连接'
    },
    login:{
      loginAniTalk: '登陆AniTalk',
      username: '用户名',
      password: '密码',
      rememberMe: '记住我',
      submit: '登录'
    },
    register:{
      title:'注册AniTalk',
      username: '用户名',
      password: '密码',
      confirmPassword: '确认密码',
      captcha: '验证码',
      agree: '我已阅读并同意',
      protocol: '《用户协议》',
      submit: '立即注册'
    },
    profile:{
      title: '用户中心',
      welcome: '欢迎',
      changeAvatar: '修改头像',
      changePassword: '修改密码',
      changeUsername: '修改用户名',
      confirmChange: '确认修改',
      back: '返回',
      selectNewAvatar: '选择新头像',
      cancel: '取消',
      chooseAvatar: '选择一个头像',
      newPassword: '新密码',
      confirmPassword: '确认新密码'
    }
  },
  en: {
    home: {
      title: 'Welcome to ANiTalk',
      desc: 'A brand new virtual character communication platform. Chat naturally and fun with AI characters ✨',
      start: 'Try in Browser',
      more: 'Learn More'
    },
    navbar: {
      home: 'Home',
      download: 'Download',
      login: 'Login',
      register: 'Sign Up',
      userCenter: 'User Center',
      logout: 'Logout',
    },
    download: {
      title: 'Download ANiTalk',
      desc: 'Choose your platform and start chatting with virtual characters! 🎉',
      pc: 'PC Client',
      android: 'Android APP',
      pcDesc: 'For Windows and macOS\nFull features, best experience',
      androidDesc: 'For Android devices\nChat anytime, anywhere',
      hd: 'HD Quality',
      plugin: 'Desktop Plugin',
      storage: 'Local Storage',
      fast: 'Lightweight & Fast',
      widget: 'Desktop Widget',
      cloud: 'Cloud Sync',
      downloadPC: 'Download PC Version 📥',
      downloadAndroid: 'Download Android Version 📥',
      sysreq: 'System Requirements',
      pcReq: 'PC Client',
      androidReq: 'Android APP',
      win: 'Windows 10 or later',
      mac: 'macOS 10.14 or later',
      ram4: '4GB RAM or more',
      disk2: '2GB available storage',
      andver: 'Android 8.0 or later',
      ram2: '2GB RAM or more',
      disk500: '500MB available storage',
      net: 'Network connection'
    },
    login: {
      loginAniTalk: 'Login to AniTalk',
      username: 'Username',
      password: 'Password',
      rememberMe: 'Remember me',
      submit: 'Login'
    },
    register: {
      title: 'Register AniTalk',
      username: 'Username',
      password: 'Password',
      confirmPassword: 'Confirm Password',
      captcha: 'Captcha',
      agree: 'I have read and agree to the',
      protocol: '《User Agreement》',
      submit: 'Register Now'
    },
    profile:{
      title: 'User Center',
      welcome: 'Welcome',
      changeAvatar: 'Change Avatar',
      changePassword: 'Change Password',
      changeUsername: 'Change Username',
      confirmChange: 'Confirm Change',
      back: 'Back',
      selectNewAvatar: 'Select New Avatar',
      cancel: 'Cancel',
      chooseAvatar: 'Choose an Avatar',
      newPassword: 'New Password',
      confirmPassword: 'Confirm New Password',
    }
  },
  ja: {
    home: {
      title: 'ANiTalkへようこそ',
      desc: '新しいバーチャルキャラクター交流プラットフォーム。AIキャラクターと自然で楽しい会話を楽しもう ✨',
      start: 'ブラウザで体験',
      more: 'もっと知る'
    },
    navbar: {
      home: 'ホーム',
      download: 'ダウンロード',
      login: 'ログイン',
      register: '登録',
      userCenter: 'ユーザーセンター',
      logout: 'ログアウト',
    },
    download: {
      title: 'ANiTalkをダウンロード',
      desc: 'お好きなプラットフォームを選んで、バーチャルキャラクターと楽しく会話しましょう！ 🎉',
      pc: 'PC クライアント',
      android: 'Android アプリ',
      pcDesc: 'Windows・macOS対応\n全機能・最高体験',
      androidDesc: 'Android端末対応\nいつでもどこでも会話',
      hd: '高画質',
      plugin: 'デスクトッププラグイン',
      storage: 'ローカル保存',
      fast: '軽量・高速',
      widget: 'デスクトップウィジェット',
      cloud: 'クラウド同期',
      downloadPC: 'PC版をダウンロード 📥',
      downloadAndroid: 'Android版をダウンロード 📥',
      sysreq: 'システム要件',
      pcReq: 'PC クライアント',
      androidReq: 'Android アプリ',
      win: 'Windows 10 以降',
      mac: 'macOS 10.14 以降',
      ram4: '4GB RAM 以上',
      disk2: '2GB以上の空き容量',
      andver: 'Android 8.0 以降',
      ram2: '2GB RAM 以上',
      disk500: '500MB以上の空き容量',
      net: 'ネット接続'
    },
    login: {
      loginAniTalk: 'AniTalk にログイン',
      username: 'ユーザー名',
      password: 'パスワード',
      rememberMe: 'ログイン情報を記憶する',
      submit: 'ログイン'
    },
    register: {
      title: 'AniTalkに登録',
      username: 'ユーザー名',
      password: 'パスワード',
      confirmPassword: 'パスワード確認',
      captcha: '認証コード',
      agree: '私は以下に同意します：',
      protocol: '《利用規約》',
      submit: '今すぐ登録'
    },
    profile: {
      title: 'ユーザーセンター',
      welcome: 'ようこそ',
      changeAvatar: 'アバターを変更',
      changePassword: 'パスワードを変更',
      changeUsername: 'ユーザー名を変更',
      confirmChange: '変更を確認',
      back: '戻る',
      selectNewAvatar: '新しいアバターを選択',
      cancel: 'キャンセル',
      chooseAvatar: 'アバターを選択',
      newPassword: '新しいパスワード',
      confirmPassword: '新しいパスワードを確認',
    }
  }
}

const i18n = createI18n({
  legacy: false,
  locale: 'zh',
  fallbackLocale: 'zh',
  messages
})

export default i18n 