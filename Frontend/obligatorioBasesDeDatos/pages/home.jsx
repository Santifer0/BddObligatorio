import React from "react";
import { useContext } from "react";
import { useState, useEffect } from "react";
import {Link} from "react-router-dom";
import '../components/home.css';

const Home = () => {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    fetch('http://localhost:3000/categories')
      .then(response => response.json())
      .then(data => setCategories(data))
      .catch(error => {
        console.error('Error al obtener los datos:', error);
        setCategories([]);
      });
  }, []);

  return (
    <div>
      <div className="login-wrapper">
        <div className="login-container">
            <h1>Home</h1>
                <ul>
                    {categories.map((category, index) => (
                    <li key={index}>
                        <Link to={`/QuestionPanel/${category.id}`}>
                            <button>{category.name}</button>
                        </Link>
                    </li>
                    ))}
                </ul>
                <Link to={"/CategoryAdd/"}>
                    <button className="Add a Category">Add a Category</button>
                </Link>
                <Link to={"/"}>
                    <button className="exit-button">Exit</button>
                </Link>
            </div>
        </div>
    </div>

  );
};

export default Home;