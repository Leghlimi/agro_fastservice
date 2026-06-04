  document.addEventListener("DOMContentLoaded", function () {

      AOS.init({ once: true, duration: 500, easing: 'ease-out', offset: 80 });

      // =========================================================
      // NAVBAR SHRINK ON SCROLL
      // =========================================================
      const headerEl = document.querySelector('header');
      if (headerEl) {
          window.addEventListener('scroll', function () {
              headerEl.classList.toggle('scrolled', window.scrollY > 50);
          }, { passive: true });
      }

      // =========================================================
      // RIPPLE EN BOTONES
      // =========================================================
      document.querySelectorAll('.btn-ripple').forEach(function (btn) {
          btn.addEventListener('click', function (e) {
              const rect = btn.getBoundingClientRect();
              const size = Math.max(rect.width, rect.height);
              const x = e.clientX - rect.left - size / 2;
              const y = e.clientY - rect.top  - size / 2;
              const wave = document.createElement('span');
              wave.classList.add('ripple-wave');
              wave.style.cssText = 'width:' + size + 'px;height:' + size + 'px;left:' + x + 'px;top:' + y + 'px;';
              btn.appendChild(wave);
              wave.addEventListener('animationend', function () { wave.remove(); });
          });
      });

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