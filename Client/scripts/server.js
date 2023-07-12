servers = document.getElementById("servers");

let callServer = async () => {
  let response = await fetch("http://localhost:8000/servers/");
  let data = await response.json();
  server(data);
  console.log(data);
};
callServer();

function server(data) {
  for (server of data) {
    servers.innerHTML += `
    <ul>
        <li>Name: ${server.name}</li>
        <li>Description: ${server.description}</li>
        <li>Photo: ${server.photo_main}</li>
    </ul>
    `;
  }
}
