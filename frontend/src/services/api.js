const API_URL = "http://127.0.0.1:8000/items";

export const fetchItems = async () => {
  const res = await fetch(API_URL, {
    method: "GET",
    headers: { "Content-Type": "application/json" },
    mode: "cors",  // ✅ Ensures correct CORS mode
  });
  return res.json();
};

export const createItem = async (item) => {
  const res = await fetch(API_URL, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
  return res.json();
};

export const updateItem = async (id, item) => {
  const res = await fetch(`${API_URL}/${id}`, {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(item),
  });
  return res.json();
};

export const deleteItem = async (id) => {
  const res = await fetch(`${API_URL}/${id}`, { method: "DELETE" });
  return res.json();
};
