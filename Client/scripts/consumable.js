consumables = document.getElementById("consumables");

let callConsumable = async () => {
  let response = await fetch("http://localhost:8000/consumables/");
  let data = await response.json();
  consumable(data);
  console.log(data);
};
callConsumable();

function consumable(data) {
   for (cuisine of data) {
      consumables.innerHTML += `
      <ul>
         <li>Name: ${cuisine.name}</li>
         <li>Price: ${cuisine.price}</li>
         <li>Description: ${cuisine.description}</li>
         <li>Photo: ${cuisine.photo_main}</li>
      </ul>`;
   }
}
