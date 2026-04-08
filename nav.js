// Shared Navigation Component
function createNav(activePage) {
    const pages = [
        { id: 'graph', label: 'Course Graph', href: 'index.html' },
        { id: 'abet', label: 'ABET Audit', href: 'abet.html' },
        { id: 'ai', label: 'AI & Ethics', href: 'ai-policy.html' },
        { id: 'deep', label: 'DEEP Analysis', href: 'deep-analysis.html' },
        { id: 'syllabi', label: 'Syllabus Templates', href: 'syllabi.html' },
        { id: 'cross-dept', label: 'Cross-Department', href: 'cross-dept.html' },
        { id: 'proposed', label: 'Proposed Curriculum', href: 'proposed-curriculum.html' },
    ];

    const nav = document.createElement('nav');
    nav.className = 'top-nav';
    nav.id = 'top';
    nav.innerHTML = `
        <span class="nav-brand">UMSL ME Program</span>
        ${pages.map(p =>
            `<a href="${p.href}" class="${p.id === activePage ? 'active' : ''}">${p.label}</a>`
        ).join('')}
    `;
    document.body.insertBefore(nav, document.body.firstChild);
}

// Back to Top button
function createBackToTop() {
    const btn = document.createElement('a');
    btn.className = 'back-to-top';
    btn.href = '#top';
    btn.innerHTML = '&uarr;';
    btn.title = 'Back to Top';
    document.body.appendChild(btn);

    window.addEventListener('scroll', () => {
        btn.classList.toggle('visible', window.scrollY > 300);
    });
}

// Toggle expandable sections
function toggleExpand(id) {
    const el = document.getElementById(id);
    if (el) el.classList.toggle('open');
}

// Initialize shared components
document.addEventListener('DOMContentLoaded', () => {
    createBackToTop();
});
