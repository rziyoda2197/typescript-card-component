class Card:
    def __init__(self, title, description, image_url, button_text, button_url):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.button_text = button_text
        self.button_url = button_url

    def render(self):
        html = f"""
        <div class="card">
            <img src="{self.image_url}" alt="{self.title}">
            <h2>{self.title}</h2>
            <p>{self.description}</p>
            <button><a href="{self.button_url}">{self.button_text}</a></button>
        </div>
        """
        return html

# Misol foydalanish:
card = Card(
    title="Karta",
    description="Bu karta haqida ma'lumot",
    image_url="https://example.com/image.jpg",
    button_text="Batafsil",
    button_url="https://example.com/batafsil"
)

print(card.render())
```

```typescript
interface CardProps {
  title: string;
  description: string;
  imageUrl: string;
  buttonText: string;
  buttonUrl: string;
}

class Card {
  private props: CardProps;

  constructor(props: CardProps) {
    this.props = props;
  }

  render(): string {
    return `
      <div class="card">
        <img src="${this.props.imageUrl}" alt="${this.props.title}">
        <h2>${this.props.title}</h2>
        <p>${this.props.description}</p>
        <button><a href="${this.props.buttonUrl}">${this.props.buttonText}</a></button>
      </div>
    `;
  }
}

// Misol foydalanish:
const card = new Card({
  title: "Karta",
  description: "Bu karta haqida ma'lumot",
  imageUrl: "https://example.com/image.jpg",
  buttonText: "Batafsil",
  buttonUrl: "https://example.com/batafsil"
});

console.log(card.render());
