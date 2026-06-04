  document.addEventListener("DOMContentLoaded", function () {

      AOS.init({ once: true, duration: 500, easing: 'ease-out', offset: 80 });

      // =========================================================
      // MODO OSCURO
      // =========================================================
      const btn = document.getElementById("toggle-theme");
      const html = document.documentElement;

      // Recuperar el tema guardado en localStorage al cargar la página
      const savedTheme = localStorage.getItem("theme");
      if (savedTheme) {
          html.setAttribute("data-bs-theme", savedTheme);
      }

      if (btn) {
          btn.addEventListener("click", function () {
              const current = html.getAttribute("data-bs-theme");
              const next = current === "dark" ? "light" : "dark";
              html.setAttribute("data-bs-theme", next);
              localStorage.setItem("theme", next);
          });
      }

      // =========================================================
      // MENSAJES FLOTANTES (TOASTS)
      // =========================================================
      const toastElList = [].slice.call(document.querySelectorAll('.toast'));
      toastElList.forEach(function (toastEl) {
          const toast = new bootstrap.Toast(toastEl, { delay: 3000 });
          toast.show();
      });

  });

  // =========================================================
  // MOSTRAR / OCULTAR CONTRASEÑA
  // =========================================================
  function togglePassword(fieldId) {
      const field = document.getElementById(fieldId);
      const icon = document.getElementById('icon-' + fieldId);
      if (!field || !icon) return;
      if (field.type === "password") {
          field.type = "text";
          icon.classList.replace('fa-eye', 'fa-eye-slash');
      } else {
          field.type = "password";
          icon.classList.replace('fa-eye-slash', 'fa-eye');
      }
  }