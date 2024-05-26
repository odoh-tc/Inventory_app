import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import NavBar from "./componenets/NavBar";
import { ProductProvider } from "./componenets/ProductContext";
import ProductsTable from "./componenets/ProductsTable";
import AddProducts from "./componenets/AddProducts";
import UpdateProduct from "./componenets/UpdateProduct";
import { UpdateProductContextProvider } from "./componenets/UpdateProductContext";
import { SupplierContextProvider } from "./componenets/SupplierContext";
import SupplierPage from "./componenets/SupplierPage";

function App() {
  return (
    <div>
      <Router>
        <ProductProvider>
          <NavBar />
          <div className="row">
            <div className="col-sm-10 col-xm-12 mr-auto ml-auto mt-4 mb-4">
              <UpdateProductContextProvider>
                <SupplierContextProvider>
                  <Routes>
                    <Route path="/" element={<ProductsTable />} />
                    <Route path="/updateproduct" element={<UpdateProduct />} />
                    <Route path="/supplierpage" element={<SupplierPage />} />
                    <Route path="/addproduct" element={<AddProducts />} />
                  </Routes>
                </SupplierContextProvider>
              </UpdateProductContextProvider>
            </div>
          </div>
        </ProductProvider>
      </Router>
    </div>
  );
}

export default App;
