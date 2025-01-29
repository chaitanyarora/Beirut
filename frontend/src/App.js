import React, { useState, useEffect } from "react";
import { fetchItems, createItem, updateItem, deleteItem } from "./services/api";

function App() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [description, setDescription] = useState("");

  useEffect(() => {
    loadItems();
  }, []);

  const loadItems = async () => {
    const data = await fetchItems();
    setItems(data);
  };

  const handleCreate = async () => {
    if (!name || !description) return;
    await createItem({ name, description });
    setName("");
    setDescription("");
    loadItems();
  };

  return (
    <div className="p-6 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-4 text-center">CRUD App</h1>
      
      <div className="bg-white p-4 shadow-md rounded-md max-w-lg mx-auto">
        <input
          type="text"
          placeholder="Item name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="border p-2 w-full mb-2 rounded"
        />
        <textarea
          placeholder="Item description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="border p-2 w-full mb-2 rounded"
        />
        <button
          onClick={handleCreate}
          className="bg-blue-500 text-white px-4 py-2 rounded w-full"
        >
          Add Item
        </button>
      </div>

      <div className="mt-6 grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        {items.map((item) => (
          <div key={item._id} className="bg-white p-4 shadow-md rounded-md">
            <h2 className="text-lg font-bold">{item.name}</h2>
            <p className="text-gray-600">{item.description}</p>
            <div className="mt-2 flex justify-between">
              <button
                onClick={() => deleteItem(item._id)}
                className="text-red-500"
              >
                Delete
              </button>
              <button
                onClick={() => updateItem(item._id, { name: item.name, description: "Updated description" })}
                className="text-yellow-500"
              >
                Edit
              </button>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
