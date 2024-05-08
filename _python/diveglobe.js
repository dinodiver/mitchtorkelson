// Data for the dives (you would replace this with data loaded from your CSV)
const dives = [
    { lat: 41.387999, lng: -95.049590, name: 'Atlantic Quarry', date: '7/31/18', depth: 25, time: 20 },
    { lat: -1.942460, lng: -80.788017, name: 'Reserva Marina El Pelado, Ecuador', date: '8/26/18', depth: 61, time: 40 },
    // Add more dives here...
];

// Initialize the globe
const globe = Globe()
    (document.getElementById('globeViz'))
    .globeImageUrl('//unpkg.com/three-globe/example/img/earth-night.jpg')
    .pointsData(dives)
    .pointAltitude('size')
    .pointColor(() => 'deepskyblue')
    .pointLabel(dive => `
        <strong>${dive.name}</strong><br>
        Date: ${dive.date}<br>
        Depth: ${dive.depth} ft<br>
        Time: ${dive.time} min
    `);

// Set initial camera distance
globe.cameraDistanceRadiusScale(3);
