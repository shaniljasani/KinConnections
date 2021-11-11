const MISSING_FIELD_MESSAGE = "Info not available"
const CONNECTORS_LIST = document.getElementById('connectorsList');
const SEARCH_BAR = $('#connectorsSearchBar');
const PROFESSIONAL_CATEGORIES_FILTER_SELECT = $("#professional-categories-filter");
const LANGUAGES_FILTER_SELECT = $("#languages-filter");

let connectors = [];
let searchString = "";
let languageFilter = new Set();
let professionalCategoryFilter = new Set();

PROFESSIONAL_CATEGORIES_FILTER_SELECT.on("change", (e) => {
    professionalCategoryFilter.clear();
    for (const o of e.target.selectedOptions) {
        professionalCategoryFilter.add(o.innerHTML.replace("&amp;", "&"));
    }
    filterConnectors();
});

LANGUAGES_FILTER_SELECT.on("change", (e) => {
    languageFilter.clear();
    for (const o of e.target.selectedOptions) {
        languageFilter.add(o.innerHTML);
    }
    filterConnectors();
});

SEARCH_BAR.on("keyup", (e) => {
    searchString = e.target.value.toLowerCase().trim();
    filterConnectors();
});

const filterConnectors = () => {
    let filteredConnectors = filterBySearchString(connectors);
    filteredConnectors = filterByLanguageFilter(filteredConnectors);
    filteredConnectors = filterByProfessionalCategoryFilter(filteredConnectors);

    displayConnectors(filteredConnectors);
}

const filterBySearchString = (connectors) => {
    if (searchString.length === 0) {
        return connectors;
    }

    return connectors.filter((c) => {
        return (
            c.first_name.toLowerCase().includes(searchString) ||
            c.last_name.toLowerCase().includes(searchString) ||
            c.education.toLowerCase().includes(searchString) ||
            c.bio.toLowerCase().includes(searchString) ||
            c.location.toLowerCase().includes(searchString) ||
            c.title.toLowerCase().includes(searchString) ||
            c.region_current.toLowerCase().includes(searchString)
        );
    });   
}

const filterByLanguageFilter = (connectors) => {
    if (languageFilter.size === 0) {
        return connectors;
    }

    return connectors.filter((c) => {
        if (c.languages) {
            let matchesLanguage = false;
            c.languages.forEach((l) => {
                if (languageFilter.has(l)) {
                    matchesLanguage = true;
                }
            })
            return matchesLanguage;
        }
        return false
    });
}

const filterByProfessionalCategoryFilter = (connectors) => {
    if (professionalCategoryFilter.size === 0) {
        return connectors;
    }

    return connectors.filter((c) => {
        if (c.professional_category) {
            let matchesProfessionalCategory = false;
            c.professional_category.forEach((l) => {
                console.log(l);
                if (professionalCategoryFilter.has(l)) {
                    matchesProfessionalCategory = true;
                }
            })
            return matchesProfessionalCategory;
        }
        return false;
    });
}

const loadConnectors = async () => {
    try {
        const res = await fetch('/api/connectors');
        connectors = await res.json();
        displayConnectors(connectors);
    } catch (err) {
        console.error(err);
    }
};

const displayConnectors = (connectors) => {
    const htmlString = connectors
        .map((connector) => {
            return `
            <li class="p-2 portfolio-item">
                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="${connector['images'] ? connector['images'] : "static/img/profile.png"}" alt="Image of ${connector['first_name']} ${connector['last_name']}">
                    <div class="card-body">
                        <h5 class="card-title text-center">${connector['first_name']} ${connector['last_name']}</h5>
                        <p class="card-text text-left mb-3">
                            <i class="bi bi-book-fill m-1"></i> ${connector['education'] ? connector['education'] : MISSING_FIELD_MESSAGE} <br>
                            <i class="bi bi-geo-alt-fill m-1"></i> ${connector['location'] ? connector['location'] : MISSING_FIELD_MESSAGE} <br>
                            <i class="bi bi-flag-fill m-1"></i> ${connector['region_current'] ? connector['region_current'] : MISSING_FIELD_MESSAGE}<br>
                            <i class="bi bi-filter-circle-fill m-1"></i> ${connector['professional_category'] ? connector['professional_category'].join(', ') : MISSING_FIELD_MESSAGE} <br>
                            <i class="bi bi-globe2 m-1"></i> ${connector['languages'] ? connector['languages'].join(', ') : MISSING_FIELD_MESSAGE}
                        </p>
                        <p class="text-center mx-0 my-0">
                            <a href="/connector/${connector['id']}" class="btn btn-primary">More Info</a>
                        </p>
                    </div>
                </div>
            </li>`;
        })
        .join('');
    CONNECTORS_LIST.innerHTML = htmlString;
};

const loadSelect = () => {
    let professionalCategories = new Set();
    let languageCategories = new Set();

    connectors.forEach((c) => {
        if (c['professional_category']) {
            c['professional_category'].forEach((category) => {
                professionalCategories.add(category);
            })
        }
        
        if (c['languages']) {
            c['languages'].forEach((language) => {
                languageCategories.add(language);
            })
        }
    });

    professionalCategories.forEach((c) => {
        PROFESSIONAL_CATEGORIES_FILTER_SELECT.append(`<option value="${c}">${c}</option>`)
    });
    languageCategories.forEach((c) => {
        LANGUAGES_FILTER_SELECT.append(`<option value="${c}">${c}</option>`)
    })
}

$(document).ready(async function() {
    await loadConnectors();
    loadSelect();
    $('#professional-categories-filter').select2({
        placeholder: "Filter professional category",
        allowClear: true
    });
    $('#languages-filter').select2({
        placeholder: "Filter language",
        allowClear: true
    });
});
