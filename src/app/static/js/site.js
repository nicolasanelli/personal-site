alternateStyle = () => {
  var bodyEl = document.getElementsByTagName("body")[0];
  bodyEl.classList.toggle('matrix-theme');
}

copyToClipboard = (str) => {
  const el = document.createElement('textarea');
  el.value = str;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
};