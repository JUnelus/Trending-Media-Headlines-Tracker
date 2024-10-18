const API_URL = "https://tzp238azja.execute-api.us-east-1.amazonaws.com";  // Replace with your API Gateway URL

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
