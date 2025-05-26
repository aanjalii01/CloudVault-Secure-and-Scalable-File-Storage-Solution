document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('chat-form');
  const input = document.getElementById('user-input'); // fixed ID here
  const chatbox = document.getElementById('chatbox');  // fixed ID here
  const submitBtn = form.querySelector('button[type="submit"]');

  input.focus();

  input.addEventListener('keydown', e => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      form.dispatchEvent(new Event('submit'));
    }
  });

  form.addEventListener('submit', async e => {
    e.preventDefault();

    const message = input.value.trim();
    if (!message) return;

    // User message
    const userMsgDiv = document.createElement('div');
    userMsgDiv.className = 'message user-message';
    userMsgDiv.setAttribute('role', 'article');
    userMsgDiv.setAttribute('aria-label', 'User message');

    const userIcon = document.createElement('i');
    userIcon.className = 'fas fa-smile icon';
    userIcon.setAttribute('aria-hidden', 'true');
    userMsgDiv.appendChild(userIcon);

    const userText = document.createElement('div');
    userText.className = 'text';
    userText.textContent = message;
    userMsgDiv.appendChild(userText);

    chatbox.appendChild(userMsgDiv);
    smoothScrollToBottom(chatbox);

    input.value = '';
    input.disabled = true;
    submitBtn.disabled = true;

    // Typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'message bot-message typing-message';
    typingDiv.setAttribute('role', 'article');
    typingDiv.setAttribute('aria-label', 'Bot is typing');

    typingDiv.innerHTML = `
      <i class="fas fa-robot icon" aria-hidden="true"></i>
      <div class="typing"><span></span><span></span><span></span></div>
    `;
    chatbox.appendChild(typingDiv);
    smoothScrollToBottom(chatbox);

    try {
      console.log('Sending message:', message);
      const response = await fetch('/chatbot/api', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message})
      });

      console.log('Response status:', response.status);
      const data = await response.json();
      console.log('Bot reply:', data.reply);

      await delay(600);

      typingDiv.remove();

      // Bot reply
      const botMsgDiv = document.createElement('div');
      botMsgDiv.className = 'message bot-message';
      botMsgDiv.setAttribute('role', 'article');
      botMsgDiv.setAttribute('aria-label', 'Bot message');

      const botIcon = document.createElement('i');
      botIcon.className = 'fas fa-robot icon';
      botIcon.setAttribute('aria-hidden', 'true');
      botMsgDiv.appendChild(botIcon);

      const botText = document.createElement('div');
      botText.className = 'text';
      botText.textContent = data.reply || "Sorry, I didn't get a response.";
      botMsgDiv.appendChild(botText);

      chatbox.appendChild(botMsgDiv);
      smoothScrollToBottom(chatbox);

    } catch (err) {
      console.error('Error in chatbot request:', err);
      typingDiv.remove();

      const errorDiv = document.createElement('div');
      errorDiv.className = 'message bot-message';
      errorDiv.setAttribute('role', 'alert');
      errorDiv.setAttribute('aria-live', 'assertive');

      const errorIcon = document.createElement('i');
      errorIcon.className = 'fas fa-robot icon';
      errorIcon.setAttribute('aria-hidden', 'true');
      errorDiv.appendChild(errorIcon);

      const errorText = document.createElement('div');
      errorText.className = 'text';
      errorText.textContent = "Sorry, something went wrong. Try again later.";
      errorDiv.appendChild(errorText);

      chatbox.appendChild(errorDiv);
      smoothScrollToBottom(chatbox);
    } finally {
      input.disabled = false;
      submitBtn.disabled = false;
      input.focus();
    }
  });

  function smoothScrollToBottom(element) {
    element.scrollTo({ top: element.scrollHeight, behavior: 'smooth' });
  }

  function delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
});
