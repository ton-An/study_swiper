<p align="center">
  <img src="logo.png" width="350" alt="Study Swiper Logo" />
</p>

<p align="center">
  <strong>Download your flashcard decks from StudySmarter (Vaia) to use them offline or import into other apps like Anki</strong>
</p>

<p align="center">
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License" />
  </a>
  <a href="https://github.com/ton-An/study_swiper/stargazers">
    <img src="https://img.shields.io/github/stars/ton-An/study_swiper?style=social" alt="GitHub Stars" />
  </a>
</p>

> **⚠️ Important Notice**\
> Currently, only StudySmarter email/password login is supported. Social logins
> (Google, Facebook, Apple) are not compatible.
>
> **Workaround:** Create a new StudySmarter account using email/password
> specifically for downloading decks.

## ✨ Features

- ✅ **Download flashcard decks** from StudySmarter
- 🖼️ **Save all images** from your flashcards automatically
- 📄 **Export to CSV format** compatible with Anki and other flashcard apps
- 🏷️ **Preserve tags** in an organized format

---

## 🚀 Quick Start

### 🍎 MacOS Video Tutorial
https://github.com/user-attachments/assets/9f9c45c7-f598-43be-ad0d-5553b7efa9f4

### 📥 1. Download

Visit the [Releases page](https://github.com/ton-An/study_swiper/releases) and
download the appropriate file:

- 🪟 **Windows:** `study_swiper-windows-x86_64.zip`
- 🍎 **Mac (M-Series):** `study_swiper-macos-arm64.tar.gz`
- 🍎 **Mac (Intel):** `study_swiper-macos-x86_64.tar.gz`
- 🐧 **Linux:** `study_swiper-linux-x86_64.tar.gz`

### 🔧 2. Setup (Mac/Linux only)

Make the file executable:

```bash
chmod +x study_swiper
```

### 🔍 3. Find Your Deck IDs

1. Open StudySmarter in your browser
2. Navigate to the deck you want to download
3. Copy the deck ID from the URL:

```
https://app.vaia.com/studyset/934059?trackingSource=studysets_library
                              ^^^^^^
                             Deck ID 📝
```

### 💻 4. Run the Tool

**🎯 Interactive mode:**

```bash
./study_swiper run
```

The tool will prompt you for:

- 👤 Username
- 🔐 Password (hidden input)
- 📚 Deck IDs (space-separated)

**⚡ Command line mode:**

```bash
./study_swiper run 934059 123456 --username ted --password mosbius123
```

---

## 📁 Output Structure

Downloaded files are organized as follows:

```
📂 934059/
├── 📄 934059.csv      # Flashcard data
├── 🖼️ image1.jpg      # Downloaded images
├── 🖼️ image2.png
└── ...
```

---

## 📥 Importing to Anki

### 🖼️ Step 1: Copy Images

Copy the downloaded images (not the containing folder) to your Anki media
folder:

- 🪟 **Windows:** `%APPDATA%\Anki2\User 1\collection.media\`
- 🍎 **Mac:** `~/Library/Application Support/Anki2/User 1/collection.media/`
- 🐧 **Linux:** `~/.local/share/Anki2/User 1/collection.media/`

### 📝 Step 2: Import CSV

1. Open Anki Desktop
2. Go to **File → Import...**
3. Select your CSV file (e.g., `934059.csv`)
4. Configure import settings:
   - **Field separator:** Comma
   - **Field mapping:**
     - Field 1 → Front
     - Field 2 → Back
     - Field 3 → Tags
5. Click **Import**

🎉 **That's it!** Your cards should now appear in Anki with all images working.

---

## 📊 Progress Indicators

The tool displays real-time progress:

- 🔐 **Authenticating** → ✅ Authentication successful
- 📥 **Fetching decks** → ✅ Decks successfully fetched
- 🔄 **Parsing deck** → ✅ Decks successfully parsed
- 🖼️ **Fetching images** → ✅ Images successfully saved
- 💾 **Saving to CSV** → ✅ Decks successfully saved to CSV

---

## 🔧 Troubleshooting

### ❗ Common Issues

**"Command not found"**

- Ensure you're in the same directory as the downloaded file
- Use `./study_swiper` (include the `./` prefix)

**"Permission denied"**

- Make the file executable: `chmod +x study_swiper`

**"Authentication failed"**

- Verify your StudySmarter email and password
- Ensure you're not using social login credentials

### 💡 Pro Tips

- 🚀 Download multiple decks by listing all IDs in one command
- 📊 Try downloading one deck at a time if multiple decks fail

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'feat: add amazing feature'`
   - Please follow
     [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

### 💭 Contribution Ideas

- Support for other sign in providers
- Improve error handling and user feedback
- Support for additional export formats
- Enhanced documentation

---

## 🐛 Reporting Issues

Found a bug or need a feature?
[Create an issue on GitHub](https://github.com/ton-An/study_swiper/issues)! 🚀

### 📝 Bug Report Template

```markdown
**Description:** Brief description of the problem

**Steps to Reproduce:**

1. Run command `./study_swiper run 12345`
2. Enter credentials
3. Observe error

**Expected vs Actual Behavior:** What should happen vs what actually happened

**Error Message:** [Paste the complete error message]

**System Information:**

- OS: [Windows 10 / macOS 12.1 / Ubuntu 20.04]
- Tool version: [e.g., 1.0.0]
```

### ✨ Feature Request Template

```markdown
**Feature Description:** What functionality would you like to see?

**Use Case:** Why would this be helpful?

**Example:** How would it work in practice?
```

### 🏷️ Issue Labels

- 🐛 **bug** - Something isn't working
- ✨ **enhancement** - New feature request
- 📚 **documentation** - Documentation improvements
- ❓ **question** - Questions about usage
- 👍 **good first issue** - Good for newcomers

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file
for details.

**What this means:**

- ✅ Free for personal and commercial use
- ✅ Modify and redistribute freely
- ✅ Private use allowed
- ⚠️ No warranty provided
- 📝 Must include license when redistributing

---

<div align="center">
  <strong>Happy studying! 📚✨</strong>
</div>
