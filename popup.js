document.addEventListener('DOMContentLoaded', async function() {
  try {
    // 获取当前标签页信息
    const [tab] = await chrome.tabs.query({active: true, currentWindow: true});
    const url = tab.url;
    const title = tab.title;

    // 设置网站名称
    document.getElementById('siteName').textContent = title;

    // 设置网站图标
    const favicon = document.getElementById('favicon');
    favicon.src = `chrome://favicon/size/32/${url}`;

    // 生成二维码
    new QRCode(document.getElementById('qrcode'), {
      text: url,
      width: 200,
      height: 200,
      colorDark: '#000000',
      colorLight: '#ffffff',
      correctLevel: QRCode.CorrectLevel.H
    });

    // 保存二维码功能
    document.getElementById('saveBtn').addEventListener('click', function() {
      const canvas = document.querySelector('#qrcode canvas');
      const link = document.createElement('a');
      link.download = `${title.slice(0, 30)}_qrcode.png`;
      link.href = canvas.toDataURL();
      link.click();
    });

  } catch (error) {
    console.error('Error:', error);
  }
});