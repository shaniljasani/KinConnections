const connectorsList = document.getElementById('connectorsList');
const searchBar = document.getElementById('connectorsSearchBar');
let connectors = [];

searchBar.addEventListener('keyup', (e) => {
    const searchString = e.target.value.toLowerCase().trim();

    if (searchString.length === 0) {
        displayConnectors(connectors);
        return;
    }

    const filteredConnectors = connectors.filter((connector) => {
        return (
            connector.first_name.toLowerCase().includes(searchString) ||
            connector.last_name.toLowerCase().includes(searchString) ||
            connector.education.toLowerCase().includes(searchString) ||
            connector.bio.toLowerCase().includes(searchString) ||
            connector.location.toLowerCase().includes(searchString) ||
            connector.title.toLowerCase().includes(searchString) ||
            connector.region_current.toLowerCase().includes(searchString)
        );
    });
    displayConnectors(filteredConnectors);
});

const loadConnectors = () => {
    connectorsCookieValue = getAndCleanCookie("connectors");
    connectors = JSON.parse(connectorsCookieValue);
    displayConnectors(connectors);
};

const getAndCleanCookie = (name) => {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let c = cookies[i].trim().split("=")
        if (c[0] === name) {
            c = c.slice(1, c.length + 1).join("=").split("'");
            c[0] = c[0].replace('\"', '');
            c[c.length - 1] = c[c.length - 1].replace('\"', '');
            c = c.join('"');
            c = c.replace(RegExp(/\\054/g), ",").replace(/True/g, '0');
            return c
        }
    }
    return "";
};

const displayConnectors = (connectors) => {
    const htmlString = connectors
        .map((connector) => {
            return `
            <li>
                <div class="col-lg-4 col-md-6 portfolio-item">
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
                </div>
            </li>`;
        })
        .join('');
    connectorsList.innerHTML = htmlString;
};

loadConnectors();
