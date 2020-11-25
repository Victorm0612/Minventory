export default class Bill {
    BillType = null;
    TotalPrice = null;
    Description = null;
    FkTask = null;

    constructor(billType, totalPrice, description, fkTask) {
        this.BillType = billType;
        this.TotalPrice = totalPrice;
        this.Description = description;
        this.FkTask = fkTask;
    }

    getBillType() {
        return this.BillType
    }
    getTotalPrice() {
        return this.TotalPrice
    }
    getDescription() {
        return this.Description
    }
    getFkTask() {
        return this.FkTask
    }
}