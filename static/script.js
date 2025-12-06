
const fileInput = document.querySelector('input[type="file"]');
const previewDiv = document.getElementById('preview');
const predictionDiv = document.getElementById('prediction-result');

fileInput.addEventListener('change', (e) => {

  previewDiv.innerHTML = '';


  predictionDiv.innerHTML = '';

  const imgPreview = document.createElement('img');
  imgPreview.src = URL.createObjectURL(e.target.files[0]);
  imgPreview.alt = 'Preview';
  imgPreview.style.maxWidth = '250px';
  imgPreview.style.borderRadius = '15px';
  imgPreview.style.boxShadow = '0 4px 10px rgba(0,0,0,0.2)';
  imgPreview.style.display = 'block';
  imgPreview.style.margin = '20px auto';

  previewDiv.appendChild(imgPreview);
});

