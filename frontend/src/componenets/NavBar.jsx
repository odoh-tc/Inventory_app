import React, { useContext, useState } from "react";
import { Navbar, Nav, Form, FormControl, Button, Badge } from "react-bootstrap";
import { Link } from "react-router-dom";
import { ProductContext } from "./ProductContext";

const NavBar = () => {
  const [search, setSearch] = useState("");
  const [products, setProducts] = useContext(ProductContext);

  const updateSearch = (e) => {
    setSearch(e.target.value);
  };

  const filterProduct = (e) => {
    e.preventDefault();
    const product = products.data.filter((product) =>
      product.name.toLowerCase().includes(search.toLowerCase())
    );
    setProducts({ data: product });
  };

  return (
    <Navbar bg="dark" expand="lg" variant="dark">
      <Navbar.Brand
        style={{ fontSize: "2rem", fontWeight: "bold" }}
        href="#home"
      >
        Inventory Management App
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="basic-navbar-nav" />
      <Navbar.Collapse id="basic-navbar-nav">
        <Nav className="mr-auto">
          <Badge
            className="mt-2"
            variant="success"
            style={{ fontSize: "1.2rem", fontWeight: "bold" }}
          >
            Products In Stock:{" "}
            <span style={{ fontSize: "1rem", fontWeight: "normal" }}>
              {products.data.length}
            </span>
          </Badge>
        </Nav>
        <Form onSubmit={filterProduct} inline>
          <Link to="/addproduct" className="btn btn-primary btn-sm mr-2">
            Add Product
          </Link>
          <FormControl
            value={search}
            onChange={updateSearch}
            type="text"
            placeholder="Search Products"
            className="mr-2"
            style={{ fontSize: "1rem", fontWeight: "bold" }}
          />
          <Button
            type="submit"
            variant="outline-primary"
            style={{ fontSize: "1rem", fontWeight: "bold" }}
          >
            Search
          </Button>
        </Form>
      </Navbar.Collapse>
    </Navbar>
  );
};

export default NavBar;
