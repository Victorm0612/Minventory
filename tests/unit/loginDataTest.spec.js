import { shallowMount } from "@vue/test-utils";
import LoginComponent from "@/components/LoginComponent.vue";
import { expect } from "chai";


describe('Testing integrity of data() properties', () => {
    const wrapper = shallowMount(LoginComponent);
    it('should have step property', () => {
        expect(wrapper.vm.$data).to.have.property('step');
        expect(wrapper.vm.step).to.be.a('number');
    })

    it('should have email property', () => {
        expect(wrapper.vm.$data).to.have.property('email');
        expect(wrapper.vm.email).to.be.a('string');
    })

    it('should have password property', () => {
        expect(wrapper.vm.$data).to.have.property('password');
        expect(wrapper.vm.password).to.be.a('string');
    })

    it('should have show property', () => {
        expect(wrapper.vm.$data).to.have.property('show');
        expect(wrapper.vm.show).to.be.a('boolean');
    })

    it('should have dialog property', () => {
        expect(wrapper.vm.$data).to.have.property('dialog');
        expect(wrapper.vm.dialog).to.be.a('boolean');
    })

    it('should have load property', () => {
        expect(wrapper.vm.$data).to.have.property('load');
        expect(wrapper.vm.load).to.be.a('boolean');
    })

    it('should have rules property', () => {
        expect(wrapper.vm.$data).to.have.property('rules');
        expect(wrapper.vm.rules).to.be.a('object');
    })
})