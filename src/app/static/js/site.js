alternateStyle = () => {
  var bodyEl = document.getElementsByTagName("body")[0];
  bodyEl.classList.toggle('matrix-theme');
}

copyUrlToPost = (el, slug) => {
  var url = document.getElementById(`${slug}_url`).href;
  copyToClipboard(url)
  changeButton(el)
}

copyToClipboard = (str) => {
  const el = document.createElement('textarea');
  el.value = str;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
};

changeButton = (el) => {
  var oldInnerHTML = el.innerHTML;
  el.innerHTML = 'Link copiado <i class="fas fa-check"></i> '
  el.classList.add('clicked')
  setTimeout(() => {
    el.innerHTML = oldInnerHTML;
    el.classList.remove('clicked')
  }, 2500)
}