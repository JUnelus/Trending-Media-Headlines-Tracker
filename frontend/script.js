const API_URL = "YOUR_API_GATEWAY_URL";  // Replace with your API Gateway URL

async function fetchHeadlines() {
    try {
        const response = await fetch(API_URL);
        const data = await response.json();
        const headlinesList = document.getElementById('headlines');

        data.headlines.forEach((headline) => {
            let listItem = document.createElement('li');
            listItem.innerText = headline;
            headlinesList.appendChild(listItem);
        });
    } catch (error) {
        console.error('Error fetching headlines:', error);
    }
}

fetchHeadlines();
