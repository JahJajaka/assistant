

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE personas (
    persona_id SERIAL PRIMARY KEY,
    user_id INT NOT NULL,
    description TEXT NOT NULL,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE events (
    event_id SERIAL PRIMARY KEY,
    description TEXT NOT NULL,
    persona_id INT,
    occurred_at TIMESTAMP NOT NULL,
    is_finished BOOLEAN NOT NULL DEFAULT FALSE,
    FOREIGN KEY (persona_id) REFERENCES Personas(persona_id)
);

CREATE TABLE tags (
    tag_id SERIAL PRIMARY KEY,
    tag_name VARCHAR(255) NOT NULL,
    event_id INT NOT NULL,
    persona_id INT NOT NULL,
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (persona_id) REFERENCES Personas(persona_id),
    UNIQUE (tag_name, event_id, persona_id)
);

INSERT INTO users (username, password) VALUES
('user1', 'password1'),
('user2', 'password2'),
('user3', 'password3');

INSERT INTO personas (user_id, description, updated_at) VALUES
(1, 'Meet Jessica Torres. She''s a 32-year-old environmental consultant living in Seattle, Washington. Jessica stands about 5''6" tall, with a medium build and curly, shoulder-length brown hair. She often wears glasses with a subtle cat-eye frame, which suits her oval face. Her wardrobe is practical and tends toward earth tones, featuring a lot of greens and browns, which she says help her feel connected to nature.

Jessica graduated with a degree in Environmental Science from the University of Washington and is passionate about sustainable urban planning. On weekends, you can find her volunteering at the local community garden or hiking in the Cascade Mountains. Her friends describe her as thoughtful and dedicated, always ready to lend a hand or an ear.

Her typical day starts with a brisk walk with her rescue dog, a lively beagle named Max, followed by a quick breakfast of homemade granola and a cup of strong black coffee. In her work, she''s currently focused on a major project that aims to reduce the carbon footprint of local businesses by improving their waste management systems.

Jessica loves reading historical fiction and regularly attends a monthly book club with friends. She dreams of one day visiting the Amazon rainforest, a place she''s been fascinated by since childhood. In her community, she''s known for her annual Earth Day neighborhood cleanup initiative, which has grown in participation every year since she started it five years ago.', NOW()),
(2, 'Description for User2 Persona1', NOW()),
(1, 'Description for User1 Persona2', NOW());

INSERT INTO events (description, persona_id, occurred_at, is_finished) VALUES
('Persona creation', 1, '2023-05-01 14:00:00', FALSE),
('Event2 for Persona1', 1, '2023-05-02 14:00:00', TRUE),
('Event1 for Persona2', 2, '2023-05-01 14:00:00', FALSE);

INSERT INTO tags (tag_name, event_id, persona_id) VALUES
('Environmental Science', 1, 1),
('Seattle', 1, 1),
('Nature', 1, 1),
('Hiking', 1, 1),
('Volunteering', 1, 1),
('Reading', 1, 1),
('Pets', 1, 1),
('Sustainability', 1, 1),
('Urban Planning', 1, 1),
('Community Engagement', 1, 1),
('Tag3', 2, 1);
