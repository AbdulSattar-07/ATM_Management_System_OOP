# ATM_Management_System_OOPATM Management System using Object-Oriented Programming (OOP) in Python



## Files

- **atm_improved.py** - Improved console-based ATM (Python script)
- **app.py** - Web-based ATM using Streamlit
- **ATM.ipynb** - Original Jupyter notebook version

## Features

### Console Version (atm_improved.py)
- ✅ PIN creation with validation (4-6 digits)
- ✅ PIN change functionality
- ✅ Deposit money
- ✅ Withdraw money with balance check
- ✅ Check balance
- ✅ Looping menu (no need to restart)
- ✅ Input validation and error handling
- ✅ User-friendly messages with emojis

### Web Version (app.py)
- ✅ All console features plus:
- 📊 Transaction history with timestamps
- 📥 Export transaction history
- 🎨 Modern UI with Streamlit
- 💾 Session state management
- 🎈 Visual feedback (balloons on deposit!)
- 📱 Responsive design

## How to Run

### Console Version
```bash
python atm_improved.py
```

### Web Version
```bash
streamlit run app.py
```

## Improvements Made

### From Original ATM.ipynb:

1. **Fixed typos**: "Enters" → "Enter", "Deposite" → "Deposit", "Widthdraw" → "Withdraw"
2. **Added PIN validation**: Must be 4-6 digits, numeric only
3. **Added input validation**: Checks for valid amounts, prevents negative values
4. **Looping menu**: No need to restart after each action
5. **Better error handling**: Try-except blocks for invalid inputs
6. **Exit functionality**: Actually exits the program now
7. **Balance display**: Shows current balance after transactions
8. **Cleaner code**: Better formatting and structure

### For app.py:

1. **Added emojis**: Better visual feedback throughout
2. **PIN length requirement**: Enforced 4-6 digit minimum
3. **Export feature**: Download transaction history as TXT
4. **Better UX**: Shows available balance before withdrawal
5. **Custom styling**: Added CSS for better appearance
6. **Balloons animation**: Celebration on successful deposit
7. **Improved messages**: More descriptive success/error messages
8. **Better organization**: Cleaner code structure

## Security Notes

This is a learning project. In a real ATM system:
- PINs would be hashed, not stored in plain text
- Would have attempt limits and lockout mechanisms
- Would use secure connections
- Would have proper authentication systems
