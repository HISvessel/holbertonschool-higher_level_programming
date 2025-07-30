#!/bin/node


/* this will touch on the concept of scopes and their functionality*/
const dog = function(name) {
    const getName = function () {
        return name;
    };
    return getName;
}

const myPet = dog("Vivie");
console.log(myPet());

/*  example #2: using objects and denser functions*/

const createPet = function (name) {
    let sex;

    const pet = {
        setName(newName) {
            name = newName;
        },

        getName() {
            return name;
        },

        getSex() {
            return sex;
        },

        setSex(newSex) {
            if (
                typeof newSex === "string" &&
                (newSex.toLowerCase() === "male" ||
            newSex.toLowerCase() === "female")
            ) {
                sex = newSex;
            }
        },
    };

    return pet;
};

const pet = createPet("Vivie");
console.log(pet.getName());
pet.setName("Oliver");
pet.setSex("male");

console.log(pet.getName());
console.log(pet.getSex());