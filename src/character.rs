use std::io;

#[derive(Debug)] // Add this line to derive the Debug trait for Character
pub struct Character {
    pub name: String,
    pub level: u32,
    pub class: String,
}

impl Character {
    pub fn new() -> Self {
        println!("Creating new character...");

        println!("Character's name: ");
        let mut name = String::new();
        let msg: &str = "Failed to read line";
        io::stdin().read_line(&mut name).expect(msg);

        println!("Enter the character's class: ");
        let mut class = String::new();
        io::stdin().read_line(&mut class).expect(msg);


        Self {
            name: name.trim().to_string(),
            level: 1,
            class: class.trim().to_string(),
        }
    }
}
