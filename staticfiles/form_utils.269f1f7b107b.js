const ICONS = [
  'fa-solid fa-book', 'fa-solid fa-laptop-code', 'fa-solid fa-code',
  'fa-solid fa-database', 'fa-solid fa-network-wired', 'fa-solid fa-brain',
  'fa-solid fa-calculator', 'fa-solid fa-chart-bar', 'fa-solid fa-chart-line',
  'fa-solid fa-flask', 'fa-solid fa-globe', 'fa-solid fa-lock',
  'fa-solid fa-microchip', 'fa-solid fa-mobile-screen', 'fa-solid fa-pen',
  'fa-solid fa-project-diagram', 'fa-solid fa-robot', 'fa-solid fa-server',
  'fa-solid fa-shield-halved', 'fa-solid fa-sitemap', 'fa-solid fa-terminal',
  'fa-solid fa-wifi', 'fa-solid fa-wrench', 'fa-solid fa-puzzle-piece',
  'fa-solid fa-graduation-cap', 'fa-solid fa-chalkboard-teacher',
  'fa-solid fa-diagram-project', 'fa-solid fa-file-code', 'fa-solid fa-gears',
  'fa-solid fa-hard-drive', 'fa-solid fa-keyboard', 'fa-solid fa-layer-group',
  'fa-solid fa-magnifying-glass', 'fa-solid fa-memory', 'fa-solid fa-pen-ruler',
  'fa-solid fa-plug', 'fa-solid fa-satellite', 'fa-solid fa-table',
  'fa-solid fa-tower-broadcast', 'fa-solid fa-user-gear', 'fa-solid fa-windows',
  'fa-brands fa-python', 'fa-brands fa-js', 'fa-brands fa-html5',
  'fa-brands fa-css3-alt', 'fa-brands fa-git-alt', 'fa-brands fa-github',
  'fa-brands fa-docker', 'fa-brands fa-linux', 'fa-brands fa-react',
  'fa-brands fa-bootstrap', 'fa-brands fa-django', 'fa-brands fa-java',
];

// Color picker sync
function initColorPickers() {
  document.querySelectorAll('input[type="color"]').forEach(function(picker) {
    const textInput = document.querySelector('input[name="' + picker.name + '_text"]');
    if (textInput) {
      picker.addEventListener('input', function() {
        textInput.value = this.value;
      });
    }
  });
}

// Icon picker
function initIconPicker() {
  const iconInput = document.getElementById('icon-input');
  const iconSearch = document.getElementById('icon-search');
  const iconGrid = document.getElementById('icon-grid');

  if (!iconInput || !iconSearch || !iconGrid) return;

  iconInput.addEventListener('input', function() {
    document.getElementById('icon-preview').className = this.value;
  });

  iconSearch.addEventListener('input', function() {
    renderIcons(this.value);
  });

  renderIcons();
}

function renderIcons(filter = '') {
  const grid = document.getElementById('icon-grid');
  if (!grid) return;
  const filtered = ICONS.filter(i => i.includes(filter.toLowerCase()));
  grid.innerHTML = filtered.map(icon => `
    <div onclick="selectIcon('${icon}')" title="${icon}"
      style="display:flex; align-items:center; justify-content:center; padding:8px; border-radius:6px; cursor:pointer; border: 1px solid #dee2e6;"
      onmouseover="this.style.background='#f0f0f0'" onmouseout="this.style.background=''">
      <i class="${icon}"></i>
    </div>
  `).join('');
}

function selectIcon(icon) {
  const iconInput = document.getElementById('icon-input');
  const iconPreview = document.getElementById('icon-preview');
  if (iconInput) iconInput.value = icon;
  if (iconPreview) iconPreview.className = icon;
}

// Random helpers
function randomColor() {
  const letters = '0123456789ABCDEF';
  let color = '#';
  for (let i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function fillRandomSelects() {
  document.querySelectorAll('select').forEach(function(select) {
    console.log('Select found:', select.name, 'Options:', select.options.length);
    if (select.options.length > 1) {
      const randomIndex = Math.floor(Math.random() * (select.options.length - 1)) + 1;
      console.log('Selecting index:', randomIndex, 'Value:', select.options[randomIndex].value);
      select.selectedIndex = randomIndex;
    }
  });
}

function fillDummyDataGeneric(overrides = {}) {
  fillRandomSelects();

  // Fill all text inputs generically
  document.querySelectorAll('input[type="text"]').forEach(function(input) {
    if (!input.readOnly && input.name !== 'csrfmiddlewaretoken') {
      input.value = overrides[input.name] || input.name + '_' + Math.floor(Math.random() * 1000);
    }
  });

  // Fill textareas
  document.querySelectorAll('textarea').forEach(function(textarea) {
    textarea.value = overrides[textarea.name] || 'Sample description for testing purposes.';
  });

  // Fill date fields
  document.querySelectorAll('input[type="date"]').forEach(function(input) {
    input.value = overrides[input.name] || '2025-06-15';
  });

  // Fill url fields
  document.querySelectorAll('input[type="url"]').forEach(function(input) {
    input.value = overrides[input.name] || 'https://github.com/PJFonseca/portfolio';
  });

  // Fill number fields
  document.querySelectorAll('input[type="number"]').forEach(function(input) {
    input.value = overrides[input.name] || Math.floor(Math.random() * 20);
  });

  // Random colors
  document.querySelectorAll('input[type="color"]').forEach(function(picker) {
    const color = randomColor();
    picker.value = color;
    const textInput = document.querySelector('input[name="' + picker.name + '_text"]');
    if (textInput) textInput.value = color;
  });

  // Random icon
  const randomIcon = ICONS[Math.floor(Math.random() * ICONS.length)];
  selectIcon(randomIcon);
}

// Init everything on page load
document.addEventListener('DOMContentLoaded', function() {
  initColorPickers();
  initIconPicker();
});