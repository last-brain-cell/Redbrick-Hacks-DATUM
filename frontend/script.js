const fetchButton = document.getElementById('fetchButton');
const fetchButton1 = document.getElementById('fetchButton1');
const fetchButton2 = document.getElementById('fetchButton2');
const fetchAlertsButton = document.getElementById('fetchAlertsButton');
const fetchRemindersButton = document.getElementById('fetchRemindersButton');
const fetchSleepData = document.getElementById('fetch-sleep-data');
const outputDiv = document.querySelector('.output');
const outputDiv1 = document.querySelector('.output1');
const outputDiv2 = document.querySelector('.output2');
const dismissButton = document.getElementById('dismissButton');
const alertsDiv = document.querySelector('.alerts');
const remindersDiv = document.querySelector('.reminders');
const sleepDataDiv = document.querySelector('.sleep-data');


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
            <img src="data:image/jpeg;base64,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" alt="Profile Picture" width="50px">
            <p>Age: ${patientProfile.age}</p>
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
            <p>Blood Glucose: ${patientVitals.blood_glucose}</p>
        `;
        outputDiv1.appendChild(patientVitalsDiv);
    } catch (error) {
        console.error('Error fetching patient vitals:', error);
    }
});

// Fetch patient location
fetchButton2.addEventListener('click', async () => {
    outputDiv2.innerHTML = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/patient/location');
        const locationData = await response.json();

        const locationDiv = document.createElement('div');
        locationDiv.className = 'location';
        locationDiv.innerHTML = `
            <p>Latitude: ${locationData.latitude}</p>
            <p>Longitude: ${locationData.longitude}</p>
        `;
        outputDiv2.appendChild(locationDiv);
    } catch (error) {
        console.error('Error fetching patient location:', error);
    }
});

// Fetch patient alerts
fetchAlertsButton.addEventListener('click', async () => {
    alertsDiv.innerHTML = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/patient/alerts');
        const alertsData = await response.json();

        for (const alert of alertsData) {
            const alertItem = document.createElement('div');
            alertItem.className = 'alert';
            alertItem.innerHTML = `
                <p>Message: ${alert}</p>
            `;
            alertsDiv.appendChild(alertItem);
        }
    } catch (error) {
        console.error('Error fetching alerts:', error);
    }
});

// Fetch patient reminders
fetchRemindersButton.addEventListener('click', async () => {
    remindersDiv.innerHTML = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/patient/reminders');
        const remindersData = await response.json();

        for (const reminder of remindersData) {
            const reminderItem = document.createElement('div');
            reminderItem.className = 'reminder';
            reminderItem.innerHTML = `
                <p>Message: ${reminder}</p>
            `;
            remindersDiv.appendChild(reminderItem);
        }
    } catch (error) {
        console.error('Error fetching reminders:', error);
    }
});

fetchSleepData.addEventListener('click', async () => {
    sleepDataDiv.innerHTML = '';

    try {
        const response = await fetch('http://127.0.0.1:8000/patient/sleep_data');
        const sleepData = await response.json();

        for (const sleep of sleepData) {
            const sleepItem = document.createElement('div');
            sleepItem.className = 'sleepEntry';
            sleepItem.innerHTML = `
                <p>${sleep}</p>
            `;
            sleepDataDiv.appendChild(sleepItem);
        }
    } catch (error) {
        console.error('Error fetching sleep data:', error);
    }
});


dismissButton.addEventListener('click', () => {
    outputDiv.innerHTML = '';
    outputDiv1.innerHTML = '';
    outputDiv2.innerHTML = '';
    alertsDiv.innerHTML = '';
    remindersDiv.innerHTML = '';
    sleepDataDiv.innerHTML = '';
});
