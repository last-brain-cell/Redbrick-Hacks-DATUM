const fetchButton = document.getElementById('fetchButton');
const fetchButton1 = document.getElementById('fetchButton1');
const fetchButton2 = document.getElementById('fetchButton2');
const outputDiv = document.querySelector('.output');
const outputDiv1 = document.querySelector('.output1');
const outputDiv2 = document.querySelector('.output2');
const dismissButton = document.getElementById('dismissButton');


// Fetch patient profile
fetchButton.addEventListener('click', async () => {
    outputDiv.innerHTML = '';

    try {
        const responseProfile = await fetch('http://127.0.0.1:8000/patient/profile');
        const patientProfile = await responseProfile.json();
        const responseVitals = await fetch('http://127.0.0.1:8000/patient/vitals');
        const patientVitals = await responseVitals.json(); // Add await here
        const responseEhr = await fetch('http://127.0.0.1:8000/patient/ehr');
        const patientEhr = await responseEhr.json(); // Add await here

        const patientDiv = document.createElement('div');
        patientDiv.className = 'patient';
        patientDiv.innerHTML = `
            <h2>${patientProfile.patient_name}</h2>
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1K8ypPsfNVQU8lVxl1i2_ajismMS_w6FA4Q&usqp=CAU" alt="Profile Picture" width="50px">
            <p>Age: ${patientProfile.Age}</p>
            <p>Diagnosis: ${patientProfile.diagnosis}</p>
            <p>Address: ${patientProfile.patient_address}</p>
            <p>Notes: ${patientProfile.notes}</p>
        `;
        outputDiv.appendChild(patientDiv);
    } catch (error) {
        console.error('Error fetching patient profile:', error);
    }
});

fetchButton1.addEventListener('click', async () => {
    outputDiv1.innerHTML = '';

    try {
        const responseVitals = await fetch('http://127.0.0.1:8000/patient/vitals');
        const patientVitals = await responseVitals.json(); // Add await here

        const patientVitalsDiv = document.createElement('div');
        patientVitalsDiv.className = 'patientVitals';
        patientVitalsDiv.innerHTML = `
            <p>Heart Rate: ${patientVitals.heart_rate}</p>
            <p>Blood Pressure: ${patientVitals.blood_pressure}</p>
            <p>SP02: ${patientVitals.spo2}</p>
        `;
        outputDiv1.appendChild(patientVitalsDiv);
    } catch (error) {
        console.error('Error fetching patient vitals:', error);
    }
});

fetchButton2.addEventListener('click', async () => {
    outputDiv1.innerHTML = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/location');
        const locationData = await response.json();

        const mapDiv = document.createElement('div');
        mapDiv.id = 'map';
        outputDiv.appendChild(mapDiv);

        // Initialize map using Leaflet
        const map = L.map('map').setView([locationData.latitude, locationData.longitude], 10);
        L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

        // Add marker for the random location
        L.marker([locationData.latitude, locationData.longitude]).addTo(map)
            .bindPopup('Random GPX Location').openPopup();
        outputDiv2.appendChild(mapDiv);
    } catch (error) {
        console.error('Error fetching patient vitals:', error);
    }
});

dismissButton.addEventListener('click', () => {
    outputDiv.innerHTML = '';
    outputDiv1.innerHTML = '';
    outputDiv2.innerHTML = '';
});
