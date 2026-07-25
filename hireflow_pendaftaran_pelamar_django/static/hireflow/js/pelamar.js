document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('registrationForm');
  if (!form) return;

  const progressBar = document.getElementById('progressBar');
  const progressText = document.getElementById('progressText');
  const controls = [...form.querySelectorAll('input:not([type="hidden"]), select, textarea')];

  const formatSize = (bytes) => bytes < 1024 * 1024
    ? `${Math.ceil(bytes / 1024)} KB`
    : `${(bytes / (1024 * 1024)).toFixed(2)} MB`;

  const updateProgress = () => {
    const completed = controls.filter((control) => {
      if (control.type === 'file') return control.files.length > 0;
      if (control.type === 'checkbox') return control.checked;
      return control.value.trim() !== '';
    }).length;
    const value = Math.round((completed / controls.length) * 100);
    progressBar.style.width = `${value}%`;
    progressText.textContent = `${value}%`;
  };

  form.addEventListener('input', updateProgress);
  form.addEventListener('change', updateProgress);
  form.addEventListener('reset', () => window.setTimeout(() => {
    document.querySelectorAll('.file-preview').forEach((preview) => preview.hidden = true);
    document.querySelectorAll('.upload-dropzone').forEach((dropzone) => dropzone.hidden = false);
    updateProgress();
  }, 0));

  document.querySelectorAll('.upload-card input[type="file"]').forEach((input) => {
    input.addEventListener('change', () => {
      const card = input.closest('.upload-card');
      const file = input.files[0];
      const dropzone = card.querySelector('.upload-dropzone');
      const preview = card.querySelector('.file-preview');
      if (!file) { dropzone.hidden = false; preview.hidden = true; return; }
      if (file.size > 2 * 1024 * 1024) {
        alert('Ukuran file maksimal 2 MB.');
        input.value = '';
        dropzone.hidden = false;
        preview.hidden = true;
        updateProgress();
        return;
      }
      preview.querySelector('.file-name').textContent = file.name;
      preview.querySelector('.file-size').textContent = formatSize(file.size);
      dropzone.hidden = true;
      preview.hidden = false;
      lucide.createIcons();
    });
  });

  updateProgress();
});
