# app.py
import streamlit as st
from datetime import datetime

# ---------------------------
# App Config
# ---------------------------
st.set_page_config(page_title="ATM Simulator", page_icon="💳", layout="centered")

# Custom CSS for better styling
st.markdown("""
<style>
    /* Main container styling */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
    }
    
    /* Card styling */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Metric cards */
    .stMetric {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 5px solid #667eea;
    }
    
    /* Form styling */
    .stForm {
        background: white;
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }
    
    /* Button styling */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }
    
    [data-testid="stSidebar"] .stRadio > label {
        color: white;
        font-weight: 600;
    }
    
    /* Header styling */
    h1, h2, h3 {
        color: white;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 10px;
        border-left: 5px solid;
    }
    
    /* Transaction history styling */
    .transaction-card {
        background: white;
        padding: 15px;
        border-radius: 10px;
        margin: 10px 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #667eea;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------
# Session State Initialization
# ---------------------------
if "pin" not in st.session_state:
    st.session_state.pin = ""           
if "balance" not in st.session_state:
    st.session_state.balance = 0
if "is_authenticated" not in st.session_state:
    st.session_state.is_authenticated = False
if "history" not in st.session_state:
    st.session_state.history = []   # transaction history

# ---------------------------
# Helpers
# ---------------------------
def log_action(action: str):
    """Add action to history with timestamp and balance."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state.history.append(f"[{timestamp}] {action} | Balance: {st.session_state.balance}")

def require_pin_set() -> bool:
    if not st.session_state.pin:
        st.warning("Please create a PIN first (Sidebar → Create PIN).")
        return False
    return True

def authenticate(pin_input: str) -> bool:
    ok = (pin_input == st.session_state.pin)
    st.session_state.is_authenticated = ok
    return ok

def reset_auth():
    st.session_state.is_authenticated = False

def success(msg: str):
    st.success(msg)

def error(msg: str):
    st.error(msg)

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("🏦 ATM Menu")
st.sidebar.markdown("---")

# Show current balance in sidebar if PIN is set
if st.session_state.pin:
    st.sidebar.success(f"💰 Balance: ${st.session_state.balance}")
    st.sidebar.markdown("---")

menu = st.sidebar.radio(
    "Choose an action:",
    [
        "🏠 Dashboard",
        "🔐 Create PIN",
        "🔄 Change PIN",
        "💵 Deposit",
        "💸 Withdraw",
        "💰 Check Balance",
        "📜 Transaction History",
        "🗑️ Reset Data"
    ],
)

st.sidebar.markdown("---")
st.sidebar.caption("🔒 Secure ATM Simulator v2.0")

# Main title with welcome message
st.title("🏦 Welcome to ATM Simulator")
st.markdown("### Your secure banking experience")

# ---------------------------
# Pages
# ---------------------------

if menu == "🏠 Dashboard":
    st.header("📊 Account Dashboard")
    
    if not st.session_state.pin:
        st.warning("⚠️ Please create a PIN to get started!")
        st.info("👉 Go to **Create PIN** in the sidebar to set up your account.")
    else:
        # Account overview cards
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                label="💰 Current Balance",
                value=f"${st.session_state.balance}",
                delta=None
            )
        
        with col2:
            st.metric(
                label="📝 Total Transactions",
                value=len(st.session_state.history)
            )
        
        with col3:
            st.metric(
                label="🔐 Account Status",
                value="Active"
            )
        
        st.markdown("---")
        
        # Recent transactions
        st.subheader("📋 Recent Transactions")
        if st.session_state.history:
            recent = list(reversed(st.session_state.history))[:5]
            for i, record in enumerate(recent, 1):
                st.markdown(f"""
                <div class="transaction-card">
                    <strong>{i}.</strong> {record}
                </div>
                """, unsafe_allow_html=True)
            
            if len(st.session_state.history) > 5:
                st.info(f"📊 Showing 5 of {len(st.session_state.history)} transactions. View all in Transaction History.")
        else:
            st.info("ℹ️ No transactions yet. Start by making a deposit!")
        
        # Quick actions
        st.markdown("---")
        st.subheader("⚡ Quick Actions")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if st.button("💵 Deposit Money", use_container_width=True):
                st.session_state.quick_action = "deposit"
        
        with col2:
            if st.button("💸 Withdraw Money", use_container_width=True):
                st.session_state.quick_action = "withdraw"
        
        with col3:
            if st.button("📜 View History", use_container_width=True):
                st.session_state.quick_action = "history"

elif menu == "🔐 Create PIN":
    st.header("🔐 Create PIN")
    
    if st.session_state.pin:
        st.info("ℹ️ You already have a PIN. Use 'Change PIN' to update it.")
    else:
        with st.form("create_pin_form", clear_on_submit=True):
            new_pin = st.text_input("Enter new PIN (4-6 digits)", type="password", max_chars=6)
            new_pin2 = st.text_input("Confirm new PIN", type="password", max_chars=6)
            submitted = st.form_submit_button("Create PIN")
            if submitted:
                if not new_pin or not new_pin2:
                    error("PIN cannot be empty.")
                elif new_pin != new_pin2:
                    error("PIN and confirmation do not match.")
                elif not new_pin.isdigit():
                    error("PIN must be numeric.")
                elif len(new_pin) < 4:
                    error("PIN must be at least 4 digits long.")
                else:
                    st.session_state.pin = new_pin
                    reset_auth()
                    success("✅ Your PIN has been created successfully!")
                    log_action("New PIN created")

elif menu == "🔄 Change PIN":
    st.header("🔄 Change PIN")
    if not require_pin_set():
        st.stop()

    with st.form("change_pin_form", clear_on_submit=True):
        old_pin = st.text_input("Enter old PIN", type="password")
        new_pin = st.text_input("Enter new PIN (4-6 digits)", type="password", max_chars=6)
        new_pin2 = st.text_input("Confirm new PIN", type="password", max_chars=6)
        submitted = st.form_submit_button("Change PIN")
        if submitted:
            if not authenticate(old_pin):
                error("❌ Invalid old PIN.")
            elif new_pin != new_pin2:
                error("❌ New PIN and confirmation do not match.")
            elif not new_pin.isdigit():
                error("❌ PIN must be numeric.")
            elif len(new_pin) < 4:
                error("❌ PIN must be at least 4 digits long.")
            else:
                st.session_state.pin = new_pin
                reset_auth()
                success("✅ Your PIN has been changed successfully!")
                log_action("PIN changed")

elif menu == "💵 Deposit":
    st.header("💵 Deposit Money")
    if not require_pin_set():
        st.stop()
    
    # Show current balance
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Current Balance", f"${st.session_state.balance}")
    with col2:
        st.metric("Total Deposits", len([h for h in st.session_state.history if "Deposited" in h]))

    st.markdown("---")
    
    with st.form("deposit_form", clear_on_submit=True):
        pin_input = st.text_input("🔐 Enter your PIN", type="password", placeholder="Enter 4-6 digit PIN")
        
        # Quick amount buttons
        st.write("💡 Quick amounts:")
        col1, col2, col3, col4 = st.columns(4)
        quick_amounts = [100, 500, 1000, 5000]
        
        amount = st.number_input("💵 Enter amount to deposit", min_value=0, step=100, help="Enter the amount you want to deposit")
        
        submitted = st.form_submit_button("💰 Deposit Now", type="primary", use_container_width=True)
        if submitted:
            if not authenticate(pin_input):
                error("❌ Invalid PIN.")
            elif amount <= 0:
                error("❌ Please enter an amount greater than 0.")
            else:
                st.session_state.balance += int(amount)
                success(f"✅ Amount ${int(amount)} deposited successfully!")
                log_action(f"Deposited ${int(amount)}")
                st.balloons()

elif menu == "💸 Withdraw":
    st.header("💸 Withdraw Money")
    if not require_pin_set():
        st.stop()

    # Show current balance with warning if low
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Available Balance", f"${st.session_state.balance}")
    with col2:
        st.metric("Total Withdrawals", len([h for h in st.session_state.history if "Withdrew" in h]))
    
    if st.session_state.balance < 100:
        st.warning("⚠️ Low balance! Consider making a deposit.")
    
    st.markdown("---")
    
    with st.form("withdraw_form", clear_on_submit=True):
        pin_input = st.text_input("🔐 Enter your PIN", type="password", placeholder="Enter 4-6 digit PIN")
        
        # Show suggested amounts based on balance
        if st.session_state.balance > 0:
            st.write("💡 Suggested amounts:")
            suggested = [min(100, st.session_state.balance), 
                        min(500, st.session_state.balance), 
                        min(1000, st.session_state.balance)]
            cols = st.columns(len(suggested))
            for i, amt in enumerate(suggested):
                with cols[i]:
                    st.caption(f"${amt}")
        
        amount = st.number_input("💸 Enter amount to withdraw", 
                                min_value=0, 
                                max_value=st.session_state.balance,
                                step=100,
                                help=f"Maximum: ${st.session_state.balance}")
        
        submitted = st.form_submit_button("💵 Withdraw Now", type="primary", use_container_width=True)
        if submitted:
            if not authenticate(pin_input):
                error("❌ Invalid PIN.")
            elif amount <= 0:
                error("❌ Please enter an amount greater than 0.")
            elif int(amount) > st.session_state.balance:
                error(f"❌ Insufficient funds. Available: ${st.session_state.balance}")
            else:
                st.session_state.balance -= int(amount)
                success(f"✅ Amount ${int(amount)} withdrawn successfully!")
                log_action(f"Withdrew ${int(amount)}")

elif menu == "💰 Check Balance":
    st.header("💰 Check Balance")
    if not require_pin_set():
        st.stop()

    with st.form("check_balance_form", clear_on_submit=True):
        pin_input = st.text_input("🔐 Enter your PIN", type="password", placeholder="Enter 4-6 digit PIN")
        submitted = st.form_submit_button("🔍 Show Balance", type="primary", use_container_width=True)
        if submitted:
            if not authenticate(pin_input):
                error("❌ Invalid PIN.")
            else:
                st.success("✅ Balance retrieved successfully!")
                
                # Display balance in a nice card
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric(label="💵 Available Balance", value=f"${st.session_state.balance}")
                with col2:
                    total_deposits = sum([int(h.split("$")[1].split()[0]) for h in st.session_state.history if "Deposited" in h]) if any("Deposited" in h for h in st.session_state.history) else 0
                    st.metric(label="📥 Total Deposits", value=f"${total_deposits}")
                with col3:
                    total_withdrawals = sum([int(h.split("$")[1].split()[0]) for h in st.session_state.history if "Withdrew" in h]) if any("Withdrew" in h for h in st.session_state.history) else 0
                    st.metric(label="📤 Total Withdrawals", value=f"${total_withdrawals}")
                
                log_action("Checked Balance")

elif menu == "📜 Transaction History":
    st.header("📜 Transaction History")
    
    if not st.session_state.history:
        st.info("ℹ️ No transactions yet. Start by making a deposit!")
    else:
        # Summary cards
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("📊 Total Transactions", len(st.session_state.history))
        with col2:
            deposits = len([h for h in st.session_state.history if "Deposited" in h])
            st.metric("📥 Deposits", deposits)
        with col3:
            withdrawals = len([h for h in st.session_state.history if "Withdrew" in h])
            st.metric("📤 Withdrawals", withdrawals)
        
        st.markdown("---")
        
        # Filter options
        filter_option = st.selectbox(
            "🔍 Filter transactions:",
            ["All", "Deposits Only", "Withdrawals Only", "Balance Checks", "PIN Changes"]
        )
        
        # Filter transactions
        filtered_history = st.session_state.history
        if filter_option == "Deposits Only":
            filtered_history = [h for h in st.session_state.history if "Deposited" in h]
        elif filter_option == "Withdrawals Only":
            filtered_history = [h for h in st.session_state.history if "Withdrew" in h]
        elif filter_option == "Balance Checks":
            filtered_history = [h for h in st.session_state.history if "Checked Balance" in h]
        elif filter_option == "PIN Changes":
            filtered_history = [h for h in st.session_state.history if "PIN" in h]
        
        st.write(f"**Showing {len(filtered_history)} transaction(s)**")
        st.divider()
        
        # Display transactions in cards
        for i, record in enumerate(reversed(filtered_history), 1):
            # Determine transaction type for icon
            if "Deposited" in record:
                icon = "📥"
                color = "#d4edda"
            elif "Withdrew" in record:
                icon = "📤"
                color = "#f8d7da"
            elif "PIN" in record:
                icon = "🔐"
                color = "#d1ecf1"
            else:
                icon = "ℹ️"
                color = "#e2e3e5"
            
            st.markdown(f"""
            <div style="background-color: {color}; padding: 15px; border-radius: 10px; margin: 10px 0; border-left: 5px solid #667eea;">
                <strong>{icon} {i}.</strong> {record}
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Export option
        col1, col2 = st.columns(2)
        with col1:
            history_text = "\n".join(reversed(st.session_state.history))
            st.download_button(
                label="📥 Download Full History",
                data=history_text,
                file_name=f"atm_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                mime="text/plain",
                use_container_width=True
            )
        with col2:
            if st.button("🔄 Refresh", use_container_width=True):
                st.rerun()

elif menu == "🗑️ Reset Data":
    st.header("�️R Reset Account Data")
    
    st.error("⚠️ **WARNING:** This action cannot be undone!")
    st.warning("This will permanently clear:")
    st.markdown("""
    - 🔐 Your PIN
    - 💰 Your balance (${})
    - 📜 All transaction history ({} transactions)
    """.format(st.session_state.balance, len(st.session_state.history)))
    
    st.markdown("---")
    
    # Confirmation checkbox
    confirm = st.checkbox("✅ I understand this action is permanent")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Reset All Data", type="primary", disabled=not confirm, use_container_width=True):
            st.session_state.pin = ""
            st.session_state.balance = 0
            st.session_state.history = []
            reset_auth()
            success("✅ All session data has been cleared.")
            st.balloons()
    with col2:
        if st.button("❌ Cancel", use_container_width=True):
            st.info("Reset cancelled.")
# streamlit run app.py