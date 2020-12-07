export default class Element {
    name = null;
    description = null;
    price = null;
    reseller = null;
    element_stock = null;
    fkInventory_id = null;
    fkTask_id = null;

    constructor(name, description, price, reseller, element_stock, fkInventory_id, fkTask_id) {
        this.name = name;
        this.description = description;
        this.price = price;
        this.reseller = reseller;
        this.element_stock = element_stock;
        this.fkInventory_id = fkInventory_id;
        this.fkTask_id = fkTask_id;
    }

    getName() {
        return this.name
    }
    getDescription() {
        return this.description
    }
    getPrice() {
        return this.price
    }
    getReseller() {
        return this.reseller
    }
    getStock() {
        return this.element_stock
    }
    getFkInventory() {
        return this.fkInventory_id
    }
    getFkTask() {
        return this.fkTask_id
    }
}