/* Open external links (playground, GitHub) in a new tab safely. */
document.addEventListener("DOMContentLoaded", function () {
  const siteHost = window.location.hostname;

  document.querySelectorAll("a[href]").forEach(function (anchor) {
    try {
      const url = new URL(anchor.href, window.location.origin);
      if (url.hostname && url.hostname !== siteHost && url.protocol.startsWith("http")) {
        anchor.setAttribute("target", "_blank");
        anchor.setAttribute("rel", "noopener noreferrer");
      }
    } catch (_error) {
      /* Ignore malformed URLs */
    }
  });
});
