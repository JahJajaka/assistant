

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


