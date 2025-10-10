# ChatRoutes Python SDK - Examples

This folder contains example notebooks and scripts demonstrating ChatRoutes features.

## 🚀 Quick Start

### Google Colab (Recommended for Video Presentations)

**ChatRoutes_Complete_Demo.ipynb** - Comprehensive feature demonstration

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/chatroutes/chatroutes-python-sdk/blob/main/examples/ChatRoutes_Complete_Demo.ipynb)

**What's Included:**
- ✅ Basic conversation management
- ✅ Message streaming
- ✅ Branching & alternative responses
- ✅ **NEW: Checkpoint system demonstration**
- ✅ Token savings calculation (60-70% reduction!)
- ✅ Cost analysis with ROI calculation
- ✅ Performance benchmarks
- ✅ Visual comparison charts
- ✅ Security & immutability features
- ✅ Best practices guide

**Perfect for:**
- Video presentations
- Sales demos
- Feature showcases
- Training materials
- API exploration

### Local Jupyter Notebook

```bash
# Install dependencies
pip install chatroutes jupyter matplotlib

# Start Jupyter
jupyter notebook

# Open ChatRoutes_Complete_Demo.ipynb
```

## 📊 What You'll Learn

### Part 1: Basic Conversation Management
- Creating conversations
- Sending messages
- Getting responses
- Understanding metadata

### Part 2: Conversation Branching
- Creating branches for alternative responses
- Exploring different conversation paths
- Comparing responses across branches

### Part 3: Building Long Conversations
- Simulating realistic long conversations
- Understanding token growth
- Preparing for checkpoint demonstrations

### Part 4: Checkpoint System (NEW!)
- Creating manual checkpoints
- Listing all checkpoints
- Understanding AI-generated summaries
- Checkpoint lifecycle operations

### Part 5: Cost Savings Analysis
- Token reduction calculations
- Cost per request comparison
- Monthly and annual savings
- ROI calculation

### Part 6: Visual Comparisons
- Token usage charts
- Cost comparison graphs
- Performance benchmarks
- Savings visualization

### Part 7: Performance Demonstration
- Response time measurement
- Checkpoint usage verification
- Context optimization metrics

### Part 8: Security Features
- Message immutability
- Cryptographic hashing
- Audit trails
- Compliance features

### Part 9: Advanced Checkpoint Operations
- Retrieving checkpoints
- Recreating checkpoints
- Managing checkpoint lifecycle

### Part 10: Scaling Analysis
- Startup scenarios
- Enterprise scenarios
- Cost projections
- Savings at scale

### Part 11: Best Practices
- Checkpoint management strategies
- Branching best practices
- Token optimization tips
- Security guidelines

## 📈 Key Metrics Demonstrated

**Cost Savings:**
- **60-70% token reduction** for conversations >150 messages
- **$17,100 annual savings** (10K conversations/month)
- **342% ROI** in first year

**Performance:**
- **2-3x faster** responses for long conversations
- **<5ms context assembly** (10x better than target)
- **Consistent performance** regardless of length

**Security:**
- **100% immutable** messages (database-enforced)
- **SHA-256 hashing** for integrity
- **Complete audit trails** for compliance

## 🎥 Using for Video Presentations

The notebook is specifically designed for video presentations:

1. **Clear Section Headings** - Easy to follow along
2. **Visual Charts** - matplotlib graphs show comparisons
3. **Step-by-Step Output** - Each cell shows results clearly
4. **Print Summaries** - Formatted boxes highlight key points
5. **No Code Editing Required** - Just run cells sequentially

### Recording Tips:

**Setup (5 minutes):**
- Open notebook in Google Colab
- Run installation cell
- Enter API key
- Initialize client

**Demo Flow (20 minutes):**
1. **Basics** (3 min) - Create conversation, send messages
2. **Branching** (3 min) - Show alternative responses
3. **Long Conversation** (4 min) - Build conversation with 20+ messages
4. **Checkpoints** (5 min) - Create, list, demonstrate savings
5. **Visualizations** (3 min) - Show charts and graphs
6. **Summary** (2 min) - Recap key benefits

**Key Talking Points:**
- "Watch how we reduce tokens by 60-70%..."
- "This translates to $17K annual savings..."
- "Responses are 2-3x faster with checkpoints..."
- "Messages are cryptographically secured and immutable..."

## 🛠️ Customization

### Change API Endpoint
```python
client = ChatRoutes(
    api_key=api_key,
    base_url="https://your-custom-endpoint.com"
)
```

### Adjust Conversation Length
```python
# In Part 3, modify the topics list
topics = [
    "Your question 1",
    "Your question 2",
    # Add more to create longer conversation
]
```

### Customize Cost Analysis
```python
# In Part 5, modify these variables
cost_per_million = 15  # Your cost per million tokens
monthly_requests = 10_000  # Your monthly volume
```

### Change Visualization Style
```python
# In Part 6, customize matplotlib settings
fig.suptitle('Your Custom Title')
ax1.set_ylabel('Your Custom Label')
```

## 📝 Other Examples

### basic_usage.py
Simple script showing basic conversation flow.

```bash
python examples/basic_usage.py
```

### checkpoint_demo.py
Focused checkpoint feature demonstration.

```bash
python examples/checkpoint_demo.py
```

### streaming_example.py
Real-time message streaming demonstration.

```bash
python examples/streaming_example.py
```

## 🐛 Troubleshooting

**"ModuleNotFoundError: No module named 'chatroutes'"**
```bash
pip install chatroutes
```

**"Authentication failed"**
- Verify your API key is correct
- Check if key has necessary permissions
- Ensure key is not expired

**"Conversation not found"**
- Make sure you're using the correct conversation_id
- Verify conversation wasn't deleted
- Check if you have access to the conversation

**Charts not displaying in Colab**
```python
# Add this at the top
%matplotlib inline
```

**Slow responses**
- Normal for first request (cold start)
- Subsequent requests should be faster
- Check your internet connection

## 📞 Support

**Documentation:** https://docs.chatroutes.com
**API Reference:** https://docs.chatroutes.com/api
**Issues:** https://github.com/chatroutes/chatroutes-python-sdk/issues
**Email:** support@chatroutes.com

## 📄 License

MIT License - see LICENSE file for details

---

**🎯 Ready to demonstrate ChatRoutes?** Open the Colab notebook and start exploring!
