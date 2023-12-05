setInterval(function () {
  console.log("hello ads nvs");
  const adContainers = document.querySelectorAll("[data-ad-size]");

  adContainers.forEach((container) => {
    const size = container.getAttribute("data-ad-size");
    fetch(`/ads/get_new_refresh?size=${size}`)
      .then((response) => response.text())
      .then((newAdHtml) => {
        data = JSON.parse(newAdHtml)
        console.log(data)
        container.innerHTML = data.new_ad_html;
      })
      .catch((error) => console.error(`Error refreshing ${size} ad:`, error));
  });
}, 30000);
