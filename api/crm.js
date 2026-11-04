// CRM Louma — reçoit les soumissions de formulaires et crée une ligne
// dans la table Supabase « leads ». Ne bloque jamais le parcours client :
// toute erreur est loggée côté serveur et répond 200.
// Env requises (Vercel) : SUPABASE_URL, SUPABASE_SERVICE_KEY
// Env optionnelles, alerte WhatsApp à Lamine pour chaque commande : CALLMEBOT_APIKEY, WHATSAPP_ALERT_PHONE

async function alerteWhatsApp(source, message) {
  const { CALLMEBOT_APIKEY: apikey, WHATSAPP_ALERT_PHONE: phone } = process.env;
  if (!apikey || !phone || !['PayPal.me', 'WhatsApp', 'Commande'].includes(source)) return;
  const text = `🛒 Commande site (${source})\n${String(message).slice(0, 1000)}`;
  try {
    const r = await fetch(`https://api.callmebot.com/whatsapp.php?phone=${encodeURIComponent(phone)}&text=${encodeURIComponent(text)}&apikey=${encodeURIComponent(apikey)}`, { signal: AbortSignal.timeout(5000) });
    if (!r.ok) console.error('Alerte WhatsApp', r.status);
  } catch (err) {
    console.error('Alerte WhatsApp', err.message);
  }
}

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ ok: false });
    return;
  }

  const { name = '', email = '', produit = '', message = '', source = 'site' } = req.body || {};

  if (!email && !message) {
    res.status(200).json({ ok: false, reason: 'empty' });
    return;
  }

  try {
    const r = await fetch(`${process.env.SUPABASE_URL}/rest/v1/leads`, {
      method: 'POST',
      headers: {
        'apikey': process.env.SUPABASE_SERVICE_KEY,
        'Authorization': `Bearer ${process.env.SUPABASE_SERVICE_KEY}`,
        'Content-Type': 'application/json',
        'Prefer': 'return=minimal'
      },
      body: JSON.stringify({
        name: String(name).slice(0, 200),
        email: String(email).slice(0, 200),
        produit: String(produit).slice(0, 500),
        message: String(message).slice(0, 2000),
        source: String(source).slice(0, 100) || 'site',
        statut: 'Nouveau'
      })
    });

    if (!r.ok) {
      console.error('Supabase error', r.status, await r.text());
    }
    await alerteWhatsApp(source, message);
    res.status(200).json({ ok: r.ok });
  } catch (err) {
    console.error('CRM error', err);
    res.status(200).json({ ok: false });
  }
};
