

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
(2, 'Meet Dave Carlson. He''s a 54-year-old corporate lawyer based in Manhattan, New York. Dave is tall, around 6''2", with a robust build and neatly combed, salt-and-pepper hair. He typically dresses in sharp, tailored suits, favoring dark colors like navy and charcoal, which match his professional demeanor.

Dave graduated from an Ivy League university with a degree in Law and has climbed the ranks to become a senior partner at his firm. He has little interest in the outdoors and spends most of his leisure time indoors, either dining at upscale restaurants or attending theater performances.

His lifestyle is fast-paced, with many evenings spent entertaining clients or working late at the office. Dave is known for his pragmatic approach to problems and isn''t one for sentimental gestures. He lives in a high-rise luxury apartment with panoramic views of the city skyline and drives a sleek, black luxury sedan.

Weekends for Dave are often about relaxation and indulgence, including enjoying fine wines and catching up on the latest stock market news. He has never owned a pet, citing allergies and a preference for a clean and orderly environment. His idea of volunteering is attending charity galas, where networking is as important as the cause.

Despite his busy schedule, Dave ensures to visit the gym regularly, focusing on strength training to maintain his physical appearance. His travels are usually business-related, though he occasionally takes exclusive vacations to places like the Hamptons or European cities. In his community, Dave is known for his contributions to local business councils and his firm''s pro bono work, though he prefers to delegate the groundwork to junior staff.', NOW()),
(1, 'Description for User1 Persona2', NOW());

INSERT INTO events (description, persona_id, occurred_at, is_finished) VALUES
('new persona created', 1, '2023-05-01 14:00:00', FALSE),
('Event2 for Persona1', 1, '2023-05-02 14:00:00', TRUE),
('new persona created', 2, '2023-05-01 14:00:00', FALSE);

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
('Corporate Law', 3, 2),
('Manhattan', 3, 2),
('Fine Dining', 3, 2),
('Theater', 3, 2),
('Luxury Lifestyle', 3, 2),
('Networking', 3, 2),
('Stock Market', 3, 2),
('Strength Training', 3, 2),
('Business Travel', 3, 2),
('Pro Bono Work', 3, 2),
('Tag3', 2, 1);
