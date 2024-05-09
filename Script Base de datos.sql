Create database IntegracionSistemaP1;
use IntegracionSistemaP1;

CREATE TABLE Ventas_Consolidadas (
    idTransaccion INT,
    idlocal INT,
    fecha DATE,
    idCategoria INT,
    idProducto INT,
    cantidad INT,
    precioUnitario DECIMAL(10, 2),
    totalVenta DECIMAL(10, 2)
);

Drop table Ventas_Consolidadas;

CREATE TABLE Ventas_Consolidadas (
    idTransaccion INT,
    fecha DATE,
    idCategoria INT,
    idProducto INT,
    cantidad INT,
    precioUnitario DECIMAL(10, 2),
    totalVenta DECIMAL(10, 2)
);