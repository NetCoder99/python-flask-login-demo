console.log("Document ready!")

document.addEventListener('DOMContentLoaded', () => {
  console.log("DOMContentLoaded was called");
});

document.addEventListener('click', e => {
  const origin = e.target.closest('a');
  if (origin) {
    console.log("link was clicked: " + origin.href);
    window.location.replace(origin.href);
//    const href = origin.href;
//    console.log(href);
//    loadProducts();
  }
});

function loadHomePage() {
  console.log("loadHomePage was called");
  window.location.replace("/home");
}

function loadProductsAjaxPage() {
  console.log("loadHomePage was called");
  window.location.replace("/data/products_ajax");
}

function loadProductsHTML() {
  console.log("loadProductsHTML was called");
  window.location.replace("/data/products");
}

function loadPandasHTML() {
  console.log("loadProductsHTML was called");
  window.location.replace("/data/pandas_demo1");
//  fetch("/data/pandas_demo1")
//  .then(res => {
//    if (res.status != 200) { throw new Error("Bad Server Response"); }
//    return res.text();
//  })
//  .then(html => {
//    //console.log(html);
//    document.body.innerHTML = html;
//  })
//  .catch(err => console.error(err));
}

function loadTabsMain() {
  console.log("loadTabsMain was called");
  window.location.replace("/tabs/tabs_main");
}
