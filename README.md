# 📚 Study Swiper

A tool that downloads your flashcard decks from StudySmarter (Vaia) to use them offline or import into other apps like Anki!

> 🚧 **Important: Email/Password Login Only**  
> Currently, only StudySmarter email/password login is supported. Social logins (Google, Facebook, Apple) won't work.  
>
> Workaround: Create a new StudySmarter account using email/password specifically for downloading decks.

## 🎯 What does it do?

This tool lets you:

- ✅ Download flashcard decks from StudySmarter  
- 🖼️ Save all images from your flashcards  
- 📄 Export to CSV format (compatible with Anki and other flashcard apps)  
- 🏷️ Keep all your tags organized  

## 🚀 Getting Started

### 📥 Step 1: Download the Tool

Go to the [Releases page](https://github.com/ton-An/study_swiper/releases) 
Download the file for your system:  
- 🪟 Windows: `study_swiper-windows-x86_64.zip`  
- 🍎 Mac: `study_swiper-macos-arm64.tar.gz` for M-Series Macs (2020 onwards) and `study_swiper-macos-x86_64.tar.gz` for Intel Macs
- 🐧 Linux: `study_swiper-linux-x86_64.tar.gz `  

### 🔧 Step 2: Make it Executable (Mac/Linux only)

Mac users:  
Bash  
```bash
chmod +x study_swiper_mac
```

Linux users:
```bash
chmod +x study_swiper_linux
```

### 🔍 Step 3: Find Your Deck IDs

Open StudySmarter in your browser  
Go to the deck you want to download  

Look at the URL – it will look like this:  
```text
https://app.vaia.com/studyset/934059?trackingSource=studysets_library
```

The deck ID is the number: 934059 📝

### 💻 Step 4: Run the Tool

**Easy mode (interactive):**  
Bash  
```bash
./study_swiper run
```

The tool will ask you for:  
- 👤 Your username  
- 🔐 Your password (hidden while typing)  
- 📚 Deck IDs (paste them separated by spaces)

**Quick mode (all at once):**  
Bash  
```bash
./study_swiper run 934059 123456 --username yourname --password yourpass
```

## 📁 Where are my files?

After downloading, you'll find:  
```
📂 934059/                (folder named after deck ID)
├── 📄 934059.csv         (your flashcards)
├── 🖼️ image1.jpg         (all images from cards)
├── 🖼️ image2.png
└── …
```
## 🎨 What you'll see while running

The tool shows progress updates:

- 🔐 **Authenticating** → ✅ Authentication successful  
- 📥 **Fetching decks** → ✅ Decks successfully fetched  
- 🔄 **Parsing deck 934059** → ✅ Decks successfully parsed  
- 🖼️ **Fetching images** → ✅ Images successfully saved  
- 💾 **Saving to CSV** → ✅ Decks successfully saved to CSV  

## ❓ Troubleshooting

**"Command not found" error:**

- Make sure you're in the same folder as the downloaded file  
- Use `./study_swiper` (with the `./` in front)

**"Permission denied" error:**

- You forgot to make it executable (see Step 2)

**"Authentication failed" error:**

- Double-check your username and password  
- Make sure you're using your StudySmarter login (not Google/Facebook login)

## 💡 Pro Tips

- 🚀 Download multiple decks at once by listing all IDs  
- 📊 The CSV files can be imported directly into Anki  
- 🖼️ All images are downloaded automatically – no broken pictures!  
- 🏷️ Tags are preserved in Anki-compatible format  

## 🆘 Need Help?

If you run into issues:

- Check the error message – it usually tells you what's wrong  
- Make sure your deck is public or you have access to it  
- Try downloading one deck at a time if multiple decks fail  


### 🐛 Reporting Issues

Found a bug or have a problem? Create an issue on GitHub!
#### 📝 How to write a good issue:

For bugs:
```markdown
**Description:**
Brief description of what went wrong

**Steps to reproduce:**
1. Run command ```./study_swiper run 12345```
2. Enter username and password
3. See error

**Expected behavior:**
What should have happened

**Actual behavior:**
What actually happened

**Error message:**
Paste the full error message here
Text Only

**System info:**
- OS: Windows 10 / macOS 12.1 / Ubuntu 20.04
- Python version: 3.9.7
- Tool version: 1.0.0
```

For feature requests:
```
**Feature description:**
What would you like the tool to do?

**Use case:**
Why would this be helpful?

**Example:**
How would it work?
```
🏷️ Issue labels we use:

    🐛 bug - Something isn't working
    ✨ enhancement - New feature request
    📚 documentation - Documentation improvements
    ❓ question - Questions about usage
    👍 good first issue - Good for newcomers


## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create your feature branch (git checkout -b feature/amazing-feature)
3. Commit your changes (git commit -m 'feat: some amazing feature') - please adhere to [conventional commits](https://www.conventionalcommits.org/en/v1.0.0/)
4. Push to the branch (git push origin feature/amazing-feature)
5. Open a Pull Request

### 💭 Ideas for contributions:
- Improve error handling and messages
    Add progress bars for large deck downloads


## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
What this means:

    ✅ Free to use for personal and commercial purposes
    ✅ Modify and distribute as you wish
    ✅ Private use allowed
    ⚠️ No warranty provided
    📝 Include the license when redistributing

Happy studying! 📖✨
