document.addEventListener("DOMContentLoaded", () => {
    const navToggle = document.querySelector("[data-nav-toggle]");
    const navPanel = document.querySelector("[data-nav-panel]");

    if (navToggle && navPanel) {
        navToggle.addEventListener("click", () => {
            const isOpen = navPanel.classList.toggle("is-open");
            navToggle.setAttribute("aria-expanded", String(isOpen));
        });
    }

    document.querySelectorAll("[data-alert-close]").forEach((button) => {
        button.addEventListener("click", () => {
            const alert = button.closest(".alert");
            if (alert) {
                alert.remove();
            }
        });
    });

    document.querySelectorAll("[data-search-input]").forEach((input) => {
        const key = input.getAttribute("data-search-input");
        const list = document.querySelector(`[data-search-list="${key}"]`);
        const emptyState = document.querySelector(`[data-search-empty="${key}"]`);

        if (!list) {
            return;
        }

        const items = Array.from(list.querySelectorAll("[data-search-item]"));
        const applyFilter = () => {
            const query = input.value.trim().toLowerCase();
            let visibleCount = 0;

            items.forEach((item) => {
                const text = (item.getAttribute("data-search-text") || "").toLowerCase();
                const matches = !query || text.includes(query);
                item.classList.toggle("is-hidden", !matches);
                if (matches) {
                    visibleCount += 1;
                }
            });

            if (emptyState) {
                emptyState.classList.toggle("is-hidden", visibleCount !== 0);
            }
        };

        input.addEventListener("input", applyFilter);
        applyFilter();
    });
});
