export default class User {
    FirstName = null;
    LastName = null;
    DocumentNumber = null;
    Phone = null;
    Email = null;
    Password = null;
    Address = null;
    Gender = null;
    Type = null;

    constructor(fname, lname, dnumber, phone, email, pass, address, gender, type) {
        this.FirstName = fname;
        this.LastName = lname;
        this.DocumentNumber = dnumber;
        this.Phone = phone;
        this.Email = email;
        this.Password = pass;
        this.Address = address;
        this.Gender = gender;
        this.Type = type;
    }

    getName() {
        return this.FirstName
    }
    getLastName() {
        return this.LastName
    }
    getDocumentNumber() {
        return this.DocumentNumber
    }
    getPhone() {
        return this.Phone
    }
    getEmail() {
        return this.Email
    }
    getPassword() {
        return this.Password
    }
    getAddress() {
        return this.Address
    }
    getGender() {
        return this.Gender
    }
    getType() {
        return this.Type
    }
}