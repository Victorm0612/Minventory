export default class User {
    Avatar = null;
    FirstName = null;
    LastName = null;
    DocumentType = null;
    DocumentNumber = null;
    Phone = null;
    Email = null;
    Password = null;
    Address = null;
    Gender = null;
    Type = null;

    constructor(avatar, fname, lname, dtnumber, dnumber, phone, email, pass, address, gender, type) {
        this.Avatar = avatar;
        this.FirstName = fname;
        this.LastName = lname;
        this.DocumentType = dtnumber;
        this.DocumentNumber = dnumber;
        this.Phone = phone;
        this.Email = email;
        this.Password = pass;
        this.Address = address;
        this.Gender = gender;
        this.Type = type;
    }

    getAvatar() {
        return this.Avatar
    }
    getName() {
        return this.FirstName
    }
    getLastName() {
        return this.LastName
    }
    getDocumentType() {
        return this.DocumentType
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