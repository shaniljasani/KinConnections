const connectorsList = document.getElementById('connectorsList');
const searchBar = $('#connectorsSearchBar');
const professionalCategoriesFilterSelect = $("#professional-categories-filter");
const languagesFilterSelect = $("#languages-filter");

let connectors = [];
let searchString = "";
let languageFilter = new Set();
let professionalCategoryFilter = new Set();

professionalCategoriesFilterSelect.on("change", (e) => {
    professionalCategoryFilter.clear();
    for (const o of e.target.selectedOptions) {
        professionalCategoryFilter.add(o.innerHTML);
    }
    filterConnectors();
});

languagesFilterSelect.on("change", (e) => {
    languageFilter.clear();
    for (const o of e.target.selectedOptions) {
        languageFilter.add(o.innerHTML);
    }
    filterConnectors();
});

searchBar.on("keyup", (e) => {
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
        let matchesLanguage = false;
        c.languages.forEach((l) => {
            if (languageFilter.has(l)) {
                matchesLanguage = true;
            }
        })
        return matchesLanguage;
    });
}

const filterByProfessionalCategoryFilter = (connectors) => {
    if (professionalCategoryFilter.size === 0) {
        return connectors;
    }

    return connectors.filter((c) => {
        let matchesProfessionalCategory = false;
        c.professional_category.forEach((l) => {
            if (professionalCategoryFilter.has(l)) {
                matchesProfessionalCategory = true;
            }
        })
        return matchesProfessionalCategory;
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
            <li class="p-2 portfolio-item w-25">
                <div class="portfolio-wrap">
                <img src="${connector['images']}" class="img-fluid" alt="">
                <div class="portfolio-info">
                    <p style="font-size: 22px; font-weight: 700; font-family: 'Montserrat', sans-serif;">
                    <a href="${connector['images']}" data-gallery="portfolioGallery" title="${connector['first_name']} ${connector['last_name']} - ${connector['title']}" class="portfolio-lightbox">
                    ${connector['first_name']} ${connector['last_name']}
                    </a>
                    <div>
                        <a href="${connector['images']}" data-gallery="portfolioGallery" title="{{connector.get('first_name', 'Error')}} {{connector.get('last_name', 'Error')}} - {{connector.get('title', 'Error')}}" class="link-preview portfolio-lightbox"><i class="bi bi-plus"></i></a>
                        <a href="/connectors/{{connector['id']}}" class="link-details" title="More Details"><i class="bi bi-link"></i></a>
                    </div>
                </div>
                </div>
            </li>`;
        })
        .join('');
    connectorsList.innerHTML = htmlString;
};

const loadSelect = () => {
    let professionalCategories = new Set();
    let languageCategories = new Set();

    connectors.forEach((c) => {
        c['professional_category'].forEach((category) => {
            professionalCategories.add(category);
        })
        c['languages'].forEach((language) => {
            languageCategories.add(language);
        })
    });

    professionalCategories.forEach((c) => {
        professionalCategoriesFilterSelect.append(`<option value="${c}">${c}</option>`)
    });
    languageCategories.forEach((c) => {
        languagesFilterSelect.append(`<option value="${c}">${c}</option>`)
    })
}

$(document).ready(async function() {
    await loadConnectors();
    loadSelect();
    $('#professional-categories-filter').select2();
    $('#languages-filter').select2();
});
