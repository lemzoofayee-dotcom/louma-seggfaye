-- CRM Louma — table des leads (commandes + newsletter)
-- À exécuter dans le SQL Editor de Supabase (projet bdfnfhqvppvhqcdnoezv).

create table if not exists leads (
  id          uuid default gen_random_uuid() primary key,
  name        text,
  email       text,
  produit     text,
  message     text,
  source      text default 'site',        -- 'Commande' ou 'Newsletter'
  statut      text default 'Nouveau',     -- Nouveau → Contacté → Confirmée → Expédiée → Client
  created_at  timestamptz default now()
);

-- Sécurité : RLS activé, aucune policy publique.
-- Seule la clé service_role (côté serveur Vercel) peut lire/écrire.
-- Le public ne peut jamais accéder aux leads.
alter table leads enable row level security;

-- Index pour trier par date d'arrivée
create index if not exists leads_created_at_idx on leads (created_at desc);
