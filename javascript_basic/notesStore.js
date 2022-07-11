'use strict';

class NotesStore {
    notes = [];
    valid_states = ['completed', 'active', 'others'];

    constructor(){
        this.notes = [];
    }

    /**
     * 
     * @param {string} state 
     * @param {string} name 
     */
    addNote(state, name) {
        try {
            if (!name || !name.trim()) throw `Name cannot be empty`;
            if (!this.valid_states.includes(state)) throw `Invalid state ${state}`;

            this.notes.push({
                state,
                name
            });
        } catch (error) {
            console.log(`Error: ${error}`);
            throw `Error: ${error}`;
        }  
    }

    /**
     * 
     * @param {string} state
     * @returns {Array<string>}
     */
    getNotes(state) {
        try {
            if (!this.valid_states.includes(state)) throw `Invalid state ${state}`;

            return this.notes.filter(n => n['state'] === state).map(nn => nn['name']);
        } catch (error) {
            console.log(`Error: ${error}`);
            //return [];
            throw `Error: ${error}`;
        }        
    }
}

function main() {
    const obj = new NotesStore();
    obj.addNote('active', 'coca-cola');
    obj.addNote('completed', 'pepsi');
    obj.addNote('active', 'fanta');
    obj.addNote('others', 'mezcal');
    const notes = obj.getNotes('foo');

    console.log(notes.join(','));
    console.log(obj.notes);
    console.log(notes.length);
}

main();